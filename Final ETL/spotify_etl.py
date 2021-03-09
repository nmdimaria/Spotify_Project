# Importing dependencies
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

from config import clientID, clientSecret

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientID,                                                            client_secret=clientSecret))

# Import data
spotify_data_a = pd.read_csv('../Data/SpotifyFeatures.csv')
spotify_data_a_df = pd.DataFrame(spotify_data_a)

spotify_data_b = pd.read_csv('https://spotifydataproject.s3.us-east-2.amazonaws.com/Dataset_1.csv')
spotify_data_b_df = pd.DataFrame(spotify_data_b)

spotify_data_b_df.head()

# ETL on tracks to add release dates to dataframe
track_ids = spotify_data_a_df['track_id']

release_dates1 = []
count = -1

# Looping through song ids in chunks to avoid errors
for id in track_ids[:30000]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates1.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_dates2 = []
count = 29999

for id in track_ids[30000:60000]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates2.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_dates3 = []
count = 59999

for id in track_ids[60000:90000]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates3.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_dates4 = []
count = 89999

for id in track_ids[90000:120000]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates4.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_dates5 = []
count = 119999

for id in track_ids[120000:150000]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates5.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_dates6 = []
count = 149999

for id in track_ids[150000:180000]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates6.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_dates7 = []
count = 179999

for id in track_ids[180000:210000]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates7.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_dates8 = []
count = 209999

for id in track_ids[210000:len(track_ids)]:
    try:
        song = sp.track(id)
        date = song['album']['release_date']
        release_dates8.append(date)
        count +=1
        #time.sleep(.5)
    except ConnectionResetError:
        print('ERROR')
        time.sleep(3)
        continue
    print(f'Row {count}')

release_test8 = release_dates7.copy()


# %%
# Creating copies to prevent overwriting
release_test1 = release_dates1.copy()
release_test2 = release_dates2.copy()
release_test3 = release_dates3.copy()
release_test4 = release_dates4.copy()
release_test5 = release_dates5.copy()
release_test6 = release_dates6.copy()
release_test7 = release_dates7.copy()
release_test8 = release_dates8.copy()

# Building master date list
release_test1.extend(release_test2)
release_test1.extend(release_test3)
release_test1.extend(release_test4)
release_test1.extend(release_test5)
release_test1.extend(release_test6)
release_test1.extend(release_test7)
release_test1.extend(release_test8)

# Adding to dataframe
spotify_data_a_df_FINAL = spotify_data_a_df.copy()
spotify_data_a_df_FINAL['release_date'] = release_test1

#Final check for accuracy
print(spotify_data_a_df_FINAL[220000:220001])

# Export to csv
spotify_data_a_df_FINAL.to_csv('../Data/SpotifyData.csv',index=False)


