# -*- coding: utf-8 -*-
# TEMP: set pwd as working directory
import sys
import numpy as np
import pandas as pd
# import seaborn as sb
# from ggplot import *
# import matplotlib.pyplot as plt
# %matplotlib inline
# plt.style.use('ggplot')

file_name = str(sys.argv[1])
column_name = str(sys.argv[2])

print file_name, column_name

data = pd.read_csv(file_name, sep='\t', encoding='utf-8')

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

'''PREREQUISITE
1. make sure strings/sentences loaded encoded in 'utf-8'
e.g.:
sentence = u'zhihu.com is the best Quora-like community in China"
or pd.read_csv('data.csv', encoding='utf-8')
2. required package
- scikit-learn
- nltk w/ models downloaded
'''

def tokenizer(sentence, remove_stop_words=True):
    '''DESCRIPTION
    - sentence - u'sample text' encoded in 'utf-8'
    > return tokens in string
    '''
    stop_words = ENGLISH_STOP_WORDS
    stemmer = SnowballStemmer('english')
    pattern = RegexpTokenizer('\w+')
    # pattern = RegexpTokenizer("[a-z']+")
    # '\w+' remove all non-letter, non-number characters
    tokens = pattern.tokenize(sentence)
    if remove_stop_words:
        clean_tokens = [word for word in tokens if word not in stop_words]
    else:
        clean_tokens = [word for word in tokens]
    # return " ".join([stemmer.stem(word) for word in tokens])
    # above return string type below return as a list
    return [stemmer.stem(word) for word in tokens]

def calculate_tf(df, column_name, use_idf=False, max_df=1.0, min_df=1, ngram_range=(1,3)):
    '''DESCRIPTION
    ngram_range=(1,3) 1 to 3 gram
    return: matrix of term frequencies, fitted data
    - df: dataframe
    - column_name - string: the doc column
    - use_idf - boolean: False/True whether we calculate TF or TF-IDF
    - max_df - float, min_df - int: threshold for handling extremely high/low frequency for words
    e.g.: min_df=10.0, a word at least show 10 times
    > ngram_range: tuple (min_n, max_n)
    The lower and upper boundary of the range of n-values for different n-grams to be extracted.
    All values of n such that min_n <= n <= max_n will be used.
    '''
    stop_words = ENGLISH_STOP_WORDS
    if use_idf:
        m = TfidfVectorizer(max_df=max_df, min_df=min_df, stop_words=stop_words, ngram_range=ngram_range, tokenizer=tokenizer)
    else:
        m = CountVectorizer(max_df=max_df, min_df=min_df, stop_words=stop_words, ngram_range=ngram_range, tokenizer=tokenizer)
    d = m.fit_transform(df[column_name])
    return m, d

def run_kmeans(data, k, scale=True):
    '''DESCRIPTION
    feed data an run kmeans with scaling
    **return**: result matrix, predicted data
    data: in this case, tfidf_d
    k: number of clusters, aka how many topics
    scale: normalize the data or not
    '''
    if scale:
        scaler = MinMaxScaler()
        data = scaler.fit_transform(data)
    m = KMeans(n_clusters=k).fit(data)
    d = m.predict(data)
    # d is the cluster label predicted, 1d array
    return m, d

def run_lda(data, n_topics):
    '''DESCRIPTION
    **return**: result matrix, predicted data
    data: tf_d
    run LatentDirichletAllocation
    n_jobs=-1, use all CPU powers
    learning_method='online' for large datasets
    '''
    m = LatentDirichletAllocation(n_topics=n_topics, n_jobs=-1, learning_method='online').fit(data)
    d = m.transform(data)
    return m, d

def return_topics_from_lda(model, feature_names, n_words):
    '''DESCRIPTION
    show top n_words from each topic, return dataframe
    - model: lda_m
    - feature_names: tf_m.get_feature_name()
    - n_words INT
    '''
    result = {
        'topic_num': [],
        'topics': [],
    }
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        # print("Topic #%d:" % topic_idx)
        result['topic_num'].append(topic_idx)
        topics_temp = ", ".join([feature_names[i] for i in topic.argsort()[:-n_words - 1:-1]])
        print [feature_names[i] for i in topic.argsort()[:-n_words - 1:-1]]
        result['topics'].append(topics_temp)
    result = pd.DataFrame(result)
    print result
    return result



def return_topics_from_kmean_clusters(cluster_labels, tf_matrix, feature_names, n_words):
    '''DESCRIPTION
    show top n_words from each topic, return dataframe
    - cluster_labels: kmeans_d
    - tf_matrix: tfidf_d
    - feature_names: tf_m.get_feature_name()
    - n_words INT
    '''
    d = pd.DataFrame(tf_matrix.toarray())
    d['c'] = cluster_labels
    d = d.groupby('c').sum().T
    result = {
        'cluster_num': [],
        'topics': [],
    }
    for col in d:
        result['cluster_num'].append(col)
        top_n = d[col].nlargest(n_words).index.tolist()
        topics_temp = ", ".join([feature_names[i] for i in top_n])
        print ", ".join([feature_names[i] for i in top_n])
        result['topics'].append(topics_temp)
    result = pd.DataFrame(result)
    print result
    return result


def extract_top_n_topics(n_topics, n_words, df, column_name, single_topic=True, max_df=1.0, min_df=1, ngram_range=(1,3)):
    '''DESCRIPTION
    extract top n topics across documents with top n_words
    associated with each topic
    - single_topic = True BOOLEAN means one doc one topic using kMeans;
    - single_topic = False BOOLEAN means one doc multiple topics using LDA;
    return: dataframes
    '''
    if single_topic:
        use_idf=True
        tfidf_m, tfidf_d = calculate_tf(df, column_name, use_idf, max_df, min_df, ngram_range)
        kmeans_m, kmeans_d = run_kmeans(tfidf_d, n_topics, scale=False)
        topic_result = return_topics_from_kmean_clusters(kmeans_d, tfidf_d, tfidf_m.get_feature_names(), n_words)
        topic_result.to_csv("topic_result_kMeans.csv", index=False, encoding='utf-8')
        df_topic_labels = pd.DataFrame(kmeans_m.labels_, columns = ['topic_num_by_kMeans'])
        result = pd.concat([df, df_topic_labels], axis=1)
        result.to_csv("result_kMeans.csv", index=False, encoding='utf-8')
        print topic_result
        return topic_result, result
    else:
        use_idf=False
        tf_m, tf_d = calculate_tf(df, column_name, use_idf, max_df, min_df, ngram_range)
        lda_m, lda_d = run_lda(tf_d, n_topics)
        topic_result = return_topics_from_lda(lda_m, tf_m.get_feature_names(), n_words)
        topic_result.to_csv("topic_result_LDA.csv", index=False, encoding='utf-8')
        df_topic_labels = pd.DataFrame(lda_d.argmax(axis=1), columns=['topic_num_by_LDA'])
        # lda_d.argmax(axis=1) return the topic with biggest confidence
        result = pd.concat([df, df_topic_labels], axis=1)
        result.to_csv("result_LDA.csv", index=False, encoding='utf-8')
        print topic_result
        return topic_result, result

extract_top_n_topics(5, 5, data, column_name, single_topic=False, max_df=0.6, min_df=10, ngram_range=(1,4))
extract_top_n_topics(5, 5, data, column_name, single_topic=True, max_df=0.6, min_df=10, ngram_range=(1,4))
