SELECT SUBSTRING_INDEX(playlist_uri, ':playlist:', -1) AS playlist_id
    , owner AS owner_id
    , streams
    , stream30s
    , dau
    , wau
    , mau
    , mau_previous_month
    , mau_both_months
    , users
    , skippers
    , owner_country
    , n_tracks
    , n_local_tracks
    , n_artists
    , n_albums
    , monthly_stream30s
    , monthly_owner_stream30s
	, LOWER(REPLACE(genre_1, '-', 'other')) AS genre_1
    , LOWER(REPLACE(genre_2, '-', 'other')) AS genre_2
    , LOWER(REPLACE(genre_3, '-', 'other')) AS genre_3
    , LOWER(REPLACE(mood_1, '-', 'other')) AS mood_1
    , LOWER(REPLACE(mood_2, '-', 'other')) AS mood_2
    , LOWER(REPLACE(mood_3, '-', 'other')) AS mood_3
	, REPLACE(REPLACE(REPLACE(REPLACE(tokens, '[]', 'other'), '[',''), ']',''), '"', '') AS tokens
    , 0.007 * stream30s AS x_estimated_revenue_usd
	, ROUND(IF(streams > 0, stream30s/streams, 0), 4) AS x_ratio_streams_above_30s_threshold
	, ROUND(IF(mau_previous_month > 0, mau_both_months/mau_previous_month, 0), 4) AS x_retention_rate_m
    -- need set threshold on mau_previous_month > 1 at least
    , ROUND(IF(users > 0, skippers/users, 0), 4) AS x_ratio_skippers_d
    , ROUND((210.0 * n_tracks)/60, 2) AS x_projected_engaging_time_in_min
    , ROUND((210.0 * n_tracks)/60/60, 2) AS x_projected_engaging_time_in_hour
    , ROUND((210.0 * n_tracks)/60/60/24, 2) AS x_projected_engaging_time_in_day
    -- 3.5 min per track length
    -- in Minute
    , ROUND(IF(users > 0, ((stream30s * 30.0)/60)/users, 0.0), 2) AS x_mininum_engaing_time_per_user
    -- above 30s as the threshold
    , CASE
		WHEN n_artists = 1 THEN 'single_artist'
        ELSE 'various_artist' END AS x_playlist_type_by_artist
	, CASE
		WHEN n_albums = 1 THEN 'single_album'
        ELSE 'various_album' END AS x_playlist_type_by_album
	, CASE
		WHEN n_artists = 1 AND n_albums = 1 THEN 'single_artist_single_album'
        WHEN n_artists = 1 AND n_albums > 1 THEN 'signle_artist_various_album'
        WHEN n_artists > 1 AND n_albums = 1 THEN 'various_artist_single_album'
        WHEN n_artists > 1 AND n_albums > 1 THEN 'various_artist_various_album'
        ELSE 'OTHER' END AS x_playlist_type_by_artist_by_album
FROM bi_hwu_schema.playlist_summary
ORDER BY 0.007 * stream30s DESC
LIMIT 500
