# Personal Thoughts - Human Perspective



https://spotifyforbrands.com/us/insight/music-streamers/

this article tells how music streamers love brands

use its data as reference for test



https://spotifyforbrands.com/us/

this is their brands portal



https://insights.spotify.com/us/2015/01/05/what-does-music-streaming-mean-for-brands/



some reference numbers

`$0.007` spotify ear per http://www.bbc.com/news/entertainment-arts-25217353





> ##### Spotify API
>
> https://developer.spotify.com/web-api/console/get-playlist/#complete
>
> OAuth Token :`BQD7Z4nJvlTesOHaXRMV-i4CibCeg-xuzzZ8nlM6wHd05yiL77nRVvMwNwHfkdNjAER3Tbfb7fy0jfRh0EDkdDVgQswDjKYuOt1gQIcHjKU9MdFbKhjrvIttsAhrKuBUuprsLF-TeeKQmnY6hrbF0kjfoyP7`
>
> didn't work
>
> return 404 except spotify playlist
>
> `https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}`
>
> ##### cURL Command
>
> ```shell
> curl -X GET "https://api.spotify.com/v1/users/7w5Bep4flavoyA0DvQIq2W/playlists/2i0HbrNwqR7TTHFFet80W6?market=US" -H "Accept: application/json" -H "Authorization: Bearer BQD7Z4nJvlTesOHaXRMV-i4CibCeg-xuzzZ8nlM6wHd05yiL77nRVvMwNwHfkdNjAER3Tbfb7fy0jfRh0EDkdDVgQswDjKYuOt1gQIcHjKU9MdFbKhjrvIttsAhrKuBUuprsLF-TeeKQmnY6hrbF0kjfoyP7"
> ```
>
> 













## Idea One - Most diverse Playlist

Clustering on 'Diversity' of a playlist

> High frequent streams playlist —> monetize for explorers then based on NLP topic over tokens

(148 / 3.5) = n_tracks = 42 tracks, with this threshold, we still have 291K+ rows, which is enough



for Ads pushing and recommendation



### Features

- number of tracks



[] filter off streams = 0, we need active playlist



#### Advanced

could build an classification engine on new playlist



## Idea Two - High Engaging Playlist

Features for engaging



### Features



[] run `describe()` to get basic stats





## Idea Three - Number Tracks

top 1000 cluster - pca

knowing the similarity



and topic cluster



![top1000_parallel_all](/Users/hwu/Dropbox/zOB_share/playlist_summary_analysis/pic/top1000_parallel_all.png)

`dau` is a good "splitor" for clusters









## Slides End

one more thing

With the given dataset - we forgot Audience!

to Buyer/Advertiser, conversion, CPA, reach/exposure are the definition



but to Audience/User —> interest, personal satisfaction, content affirmity









## Study on SpotifyBrands [https://spotifyforbrands.com/us/](https://spotifyforbrands.com/us/)

> # "YOU ARE WHAT YOU STREAM"
>
> — by Spotify Brand

**148 min**



(148 / 3.5) = n_tracks = 42 tracks



average cross-platform user spends listening, dancing or singing along to Spotify every day.

**Spotify internal data, global free users, January 2015**

> use this as benchmark for analysis, define 'success'



Active Trend

![chart-audience](/Users/hwu/Dropbox/zOB_share/playlist_summary_analysis/pic/chart-audience.png)

MOBILE INCREASING TREND

![chart-mobile](/Users/hwu/Dropbox/zOB_share/playlist_summary_analysis/pic/chart-mobile.png)





New Streaming Habits:

- Discovery
- Diversity
- Tilt

Reliables vs Explorers

> This could be an k-Mean Clustering

![Screen Shot 2017-07-14 at 7.06.56 PM](/Users/hwu/Dropbox/zOB_share/playlist_summary_analysis/pic/Screen Shot 2017-07-14 at 7.06.56 PM.png)



> So with our analysis, High Skips doesn't mean its bad for `Explorers`



## Ideas

### Key Flaws of the dataset to produce the result defining `successful`

Either we assume the audience/users are from the same/or similar demographic groups who are sharing similar tastse or "spotify behavior/spotify streaming habits"

`
