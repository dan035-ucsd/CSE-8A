### CSE 8A Project 2
### Author: Dani Nguyen
### Collaborations:

import csv
data = list(csv.reader(open("Ed Sheeran Dataset.csv")))
# track_id,album_name,album_id,release_date,popularity,explicit,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,time_signature,featured_artists,'type', duration,year,month,day_of_the_week
# 2        3          4        5            6          7        8            9      10  11       12   13          14           15               16       17     18            19               20      21      22       23   24    25

def average_col(col): #averages a column
    # 6 = popularity
    # 8 = danceability
    # 9 = energy
    # 11 = loudness
    # 13 = speechiness
    # 14 = acousticness
    # 15 = instrumentalness
    # 16 = liveness
    # 17 = valence
    # 18 = tempo
    total = 0
    for row in data[1:]:
        total += int(row[col])
    return total / len(data[1:])

def create_dict(col): #creates a dictionary of the column
    # 7 = explicit 
    # 10 = key 
    # 12 = mode
    # 19 = time_signature
    # 20 = featured_artists
    # 21 = type
    d = {}
    for row in data[1:]:
        entry = row[col]
        if entry not in d:
            d[entry] = 0
        else:
            d[entry] += 1
    return d