USE bi_hwu_schema;

CREATE TABLE IF NOT EXISTS playlist_summary (
    playlist_uri	VARCHAR(255)
    , owner	VARCHAR(255)
    , streams	BIGINT
    , stream30s	BIGINT
    , dau	BIGINT
    , wau	BIGINT
    , mau	BIGINT
    , mau_previous_month	BIGINT
    , mau_both_months	BIGINT
    , users	BIGINT
    , skippers	BIGINT
    , owner_country	VARCHAR(255)
    , n_tracks	BIGINT
    , n_local_tracks	BIGINT
    , n_artists	BIGINT
    , n_albums	BIGINT
    , monthly_stream30s	BIGINT
    , monthly_owner_stream30s	BIGINT
    , tokens	VARCHAR(255)
    , genre_1	VARCHAR(255)
    , genre_2	VARCHAR(255)
    , genre_3	VARCHAR(255)
    , mood_1	VARCHAR(255)
    , mood_2	VARCHAR(255)
    , mood_3	VARCHAR(255)
)
