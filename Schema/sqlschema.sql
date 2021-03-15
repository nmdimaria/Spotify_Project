
CREATE TABLE dataset_1 (
    "genre" varchar   NOT NULL,
    "track_id" varchar   NOT NULL,
    "popularity" float   NOT NULL,
    "acousticness" float   NOT NULL,
    "danceability" float   NOT NULL,
    "duration_ms" float   NOT NULL,
    "energy" float   NOT NULL,
    "instrumentalness" float   NOT NULL,
    "key" varchar   NOT NULL,
    "liveness" float   NOT NULL,
    "loudness" float   NOT NULL,
    "mode" varchar   NOT NULL,
    "speechiness" float   NOT NULL,
    "tempo" float   NOT NULL,
    "valence" float   NOT NULL,
    "year" float   NOT NULL,
    CONSTRAINT "pk_dataset_1" PRIMARY KEY (
        "track_id"
     )
);

CREATE TABLE dataset_2 (
    "acousticness" float   NOT NULL,
    "danceability" float   NOT NULL,
    "duration_ms" int   NOT NULL,
    "energy" float   NOT NULL,
    "explicit" int   NOT NULL,
    "id" varchar   NOT NULL,
    "instrumentalness" float   NOT NULL,
    "key" int   NOT NULL,
    "liveness" float   NOT NULL,
    "loudness" float   NOT NULL,
    "mode" int   NOT NULL,
    "popularity" int   NOT NULL,
    "release_date" varchar   NOT NULL,
    "speechiness" float   NOT NULL,
    "tempo" float   NOT NULL,
    "valence" float   NOT NULL,
    "year" int   NOT NULL,
	"bi_popularity" int NOT NULL,
    CONSTRAINT "pk_dataset_2" PRIMARY KEY (
        "id"
     )
);


CREATE TABLE popularity ( 
	"track_id" varchar NOT NULL,
	"bi_popularity" int NOT NULL,
	CONSTRAINT "pk_popularity" PRIMARY KEY (
		"track_id")
);

SELECT dataset_1.*,
	popularity.bi_popularity
INTO combined_music_pop
FROM dataset_1
JOIN popularity 
ON popularity.track_id = dataset_1.track_id;

select * from combined_music_pop;