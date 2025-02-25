### CSE 8A Project 2
### Author: Dani Nguyen
### Collaborations:

import csv
data = list(csv.reader(open("Ed Sheeran Dataset.csv")))

# how popular is each album

def average_col(col): # averages a column
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

def create_dict(col): # creates a tally of the column in dict form
    # 3 = album_name
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
            d[entry] = 1
        else:
            d[entry] += 1
    return d

def avg_col_perAlbum(col, album): # averages a column with album filter
    total = 0
    count = 0
    lst = []
    
    for row in data[1:]:         # filters column
        if row[3] == album:
            lst.append(row)
    for row in lst:              # averages column
        total += int(row[col])
        count += 1
    return total / count

def avg_col_byAlbum(col):    # averages a column for every album
    albums = list(create_dict(3).items())
    lst = []
    for (key, val) in albums:
        lst.append((avg_col_perAlbum(col,key),key)) 
    lst.sort(reverse=True)
    return lst

print(avg_col_byAlbum(6)[0])