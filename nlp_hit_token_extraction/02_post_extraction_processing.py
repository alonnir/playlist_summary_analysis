# -*- coding: utf-8 -*-
# TEMP: set pwd as working directory
import sys
import numpy as np
import pandas as pd


# JOIN TOPIC LABELS TO RESULT
# ###########################
result = pd.read_csv('result_kMeans.csv', sep=',', encoding='utf-8')
label = pd.read_csv('topic_result_kMeans.csv', sep=',', encoding='utf-8')
df = result.merge(label, how='inner', left_on='topic_num_by_kMeans', right_on='cluster_num')
# df.to_csv('result_dataTopicHierarchy201705.tsv', sep='\t', encoding='utf-8')




# RUN SENTIMENT ANALYSIS ON DOC TITLE
# ###################################
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def get_sentiment_score(sentence):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # above code make sure system default encoding as 'utf-8'
    analyzer = SentimentIntensityAnalyzer()
    sentence = str(sentence)
    sentiment_score = analyzer.polarity_scores(sentence)
    print sentiment_score
    return sentiment_score.get('compound')


df['sentiment_score'] = df['nlp_tokens'].apply(get_sentiment_score)

def is_positive(score):
    if score > 0:
        return 'postive'
    elif score == 0:
        return 'netural'
    else:
        return 'negative'

df['is_positive'] = df['sentiment_score'].apply(is_positive)
df.to_csv('result_kMeans_with_label_attached.tsv', sep='\t', encoding='utf-8')
