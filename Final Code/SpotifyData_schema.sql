-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "SpotifyFeatures" (
    "genre" string   NOT NULL,
    "artist_name" string   NOT NULL,
    "track_name" string   NOT NULL,
    "track_id" int   NOT NULL,
    "popularity" int   NOT NULL,
    "acousticness" float   NOT NULL,
    "danceability" float   NOT NULL,
    "duration_ms" int   NOT NULL,
    "energy" float   NOT NULL,
    "instrumentalness" float   NOT NULL,
    "key" string   NOT NULL,
    "liveness" float   NOT NULL,
    "loudness" float   NOT NULL,
    "mode" string   NOT NULL,
    "speechiness" float   NOT NULL,
    "tempo" float   NOT NULL,
    "time_signature" string   NOT NULL,
    "valence" float   NOT NULL,
    "release_date" string   NOT NULL,
    CONSTRAINT "pk_SpotifyFeatures" PRIMARY KEY (
        "track_id"
     )
);

