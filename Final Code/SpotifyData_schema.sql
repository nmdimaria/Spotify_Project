-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "SpotifyFeatures" (
    "genre" text   NOT NULL,
    "artist_name" text   NOT NULL,
    "track_name" text   NOT NULL,
    "track_id" int   NOT NULL,
    "popularity" int   NOT NULL,
    "acousticness" float   NOT NULL,
    "danceability" float   NOT NULL,
    "duration_ms" int   NOT NULL,
    "energy" float   NOT NULL,
    "instrumentalness" float   NOT NULL,
    "key" text   NOT NULL,
    "liveness" float   NOT NULL,
    "loudness" float   NOT NULL,
    "mode" text   NOT NULL,
    "speechiness" float   NOT NULL,
    "tempo" float   NOT NULL,
    "time_signature" text   NOT NULL,
    "valence" float   NOT NULL,
    "release_date" datetime   NOT NULL,
    "year" int  NOT NULL,
    CONSTRAINT "pk_SpotifyFeatures" PRIMARY KEY (
        "track_id"
     )
);

