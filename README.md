# Spotify_Project

### Deliverable 2: 

- Presentiation can be found at https://docs.google.com/presentation/d/1l4uSM41oqsHwszULNW9IYb_7RSEgzeA58z1-NmlePnE/edit#slide=id.p
- Our Github is up to date with all relevent content ("Final Code" folder contains ETL) AND see Data for analysis description
- SVM file is our machine learning model AND see Technologies for description
- Database SQL schema can be found in "Final Code" folder and in DB Schema

## Summary
Have you ever thought that "All pop music sounds the same"? Our final project will finally test that hypothesis...

We will be using data from Spotify's APIs combined with some external data sets to predict which songs will be popular in the future. Spotify's machine learning algorithm analyzes music to determine parameters like key, tempo, time signature, and even danceability, liveliness and popularity. This data, combined with some external data sources cataloguing popular music over the past 10 years and support vector machine learning algorithms will help us prove/disprove our hypothesis and finally put to rest that pop songs have similar, measureable characteristics and that we may even be able to predict future popularity.

Part of our presentation/visualizations will be to pick out common elements and describe them in comparison to songs that do not perform as well. Our group has a deep passion for music and we are very excited to present our findings.

#### Nick DiMaria, Will Grace and Michael Rediker

## Data
See code for examples of input data.

Spotify is a very interesting source of data for this the project. It can be very difficult to pull a large amount of random songs directly from the API, but we were able to find some people who had done it already.

We needed to suppliment the data source (the 1920-2020 dataset) with the year and release date to be able to filter the data from the past 10 years. We want to define popularity in new music only. The dataset is also quite large and we need to slim it down a bit to make our machine learning model more efficient. We filtered out some irrelevant genres like Classical and Opera because there is a good bet that most songs written for those genres were written centuries ago even if the recordings were done more recently.

Finally, the popularity measure is a number between 0 and 100. To streamline the prediction process, we converted the measure to a binary scale by classifing every song with a popularity rating 60 and above as popular (1) and everything below as unpopular (0).

Kaggle data 

https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db?select=SpotifyFeatures.csv

https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks

Some similar analysis from Kaggle
https://www.kaggle.com/cihanoklap/top-songs-on-spotify-what-makes-them-popular

Similar study
https://techxplore.com/news/2019-09-spotify-songs.html

## Technologies Employed

- Spotipy Python/API library
- Python with Pandas/Numpy etc. for ETL
- SVM, Random Forrest machine learning models
- Postgres database
- AWS cloud storage
- Tableau for visualizations

## Communication
We will be using our Slack group as well as regular Zoom meetings to coordinate as well as keeping our code on Github for collaberation

## Machine Learning Model

- We are aiming for our final ML dataset to contain about 50,000 rows. 
- The popularity measure from Spotify is on a scale from 0 (least popular) to 100 (most popular). We decided to create a cutoff in the popularity of 70 and consider everything below that threshold as unpopular and everything above as popular. This corresponds to roughly the top 10% songs. 
- The primary features from Spotify were numerical and scaled easily using the StandardScaler. 

