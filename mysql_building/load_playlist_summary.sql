USE bi_hwu_schema;

LOAD DATA LOCAL INFILE 'prod_campaign_ctr_lookup.txt'
INTO TABLE bi_hwu_schema.playlist_summary
FIELDS TERMINATED BY '\t'
IGNORE 1 LINES;
