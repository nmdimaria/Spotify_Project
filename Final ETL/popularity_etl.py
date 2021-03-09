
# To add a new markdown cell, type '# %% [markdown]'
#Import dependencies
import pandas as pd


#Importing data
spotify_data = pd.read_csv('https://spotifydataproject.s3.us-east-2.amazonaws.com/Dataset_1.csv')
spotify_data2 = pd.read_csv('https://spotifydataproject.s3.us-east-2.amazonaws.com/Dataset_2.csv')
spotify_data_df = pd.DataFrame(spotify_data)
spotify_data2_df = pd.DataFrame(spotify_data2)


#Converting to datetime
spotify_data_df['release_date'] = pd.to_datetime(spotify_data_df['release_date'], errors='coerce', format='%Y-%m-%d')

#Creating year column
spotify_data_df['year'] = pd.DatetimeIndex(spotify_data_df['release_date']).year.fillna(0.0).astype(int)

#Filtering the dataset
filtered_data_df = spotify_data_df[spotify_data_df['year'] >= 2010]
filtered_data_df = filtered_data_df.drop_duplicates(subset='track_id')
filtered_data_df = filtered_data_df[filtered_data_df['genre'] != 'Movie']
filtered_data_df = filtered_data_df[filtered_data_df['genre'] != 'Classical']
filtered_data_df = filtered_data_df[filtered_data_df['genre'] != 'Opera']
filtered_data_df = filtered_data_df[filtered_data_df['genre'] != 'Anime']

#Creating binary popularity measure
bi_popularity = []

for row in filtered_data_df['popularity']:
    if row >= 70:
        bi_popularity.append(1)
    else:
        bi_popularity.append(0)

#Creating popularity dataframe
popularity_df = pd.DataFrame(list(zip(filtered_data_df['track_id'], bi_popularity)), columns=['track_id', 'bi_popularity'])
popularity_df['bi_popularity'].value_counts()

#Exporting data
filtered_data_df.to_csv('../../Data/filtered_data.csv', index=False)
popularity_df.to_csv('../../Data/popularity.csv', index=False)

#Filtering data 2 (which was not used in ML Model)
filtered_data2_df = spotify_data2_df[spotify_data_df['year'] >= 2010]
filtered_data2_df = spotify_data2_df.drop_duplicates()
filtered_data2_df = spotify_data2_df.drop_duplicates(subset = 'id')
filtered_data2_df = filtered_data2_df.drop(columns= ['artists', 'name'])

#Creating binary popularity measure
bi_popularity2 = []

for row in filtered_data2_df['popularity']:
    if row >= 70:
        bi_popularity2.append(1)
    else:
        bi_popularity2.append(0)

#Add bi popularity
filtered_data2_df['bi_popularity'] = bi_popularity2

#Exporting data 2
filtered_data2_df.to_csv('../../Data/filtered_data2.csv', index=False)