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









## Todos

1. Review Edward Chen's [Answers on AB testing](https://www.quora.com/When-should-A-B-testing-not-be-trusted-to-make-decisions)
2. Ask Grace to add additional 30min, to ask a team member present/talk one of the ongoing project - full lifecycle, it's a two way selection `DONE`
3. Key metrics in Music Stream Industry


like soundcloud stats

![stats_overview](/Users/hwu/Dropbox/zOB_share/playlist_summary_analysis/pic/stats_overview.jpg)

![stats_overview](/Users/hwu/Dropbox/zOB_share/playlist_summary_analysis/pic/Screenshot_experiment_v5_4.png)









`mysql://bidbprodmaster:Ag4xt2UCr9bChU7vcdWFDRty@bidb-10002-prod-nydc1.nydc1.outbrain.com:3306/bi_hwu_schema`
