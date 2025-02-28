### CSE 8A Project 2
### Author: Dani Nguyen
### Collaborations: Github Copilot

import csv
data = list(csv.reader(open("Ed Sheeran Dataset.csv")))

#   num vars                    catergorical vars
    # 6 = popularity            # 3 = album_name
    # 8 = danceability          # 7 = explicit 
    # 9 = energy                # 10 = key
    # 11 = loudness             # 12 = mode
    # 13 = speechiness          # 19 = time_signature
    # 14 = acousticness         # 20 = featured_artists
    # 15 = instrumentalness     # 21 = type
    # 16 = liveness             # 23 = year
    # 17 = valence              
    # 18 = tempo                

def create_dict(col): 
    ''' 
    Given a column, returns dictionary which is a tally of said column.
    '''
    d = {}
    for row in data[1:]:
        entry = row[col]
        if entry not in d:
            d[entry] = 1
        else:
            d[entry] += 1
    return d

def avg_col_perCategory(datCol, catCol, filter):     # only works with int categories ..
    ''' 
    Given a column, a category, and a filter. Loops through a category column and 
    a data column, while filtering the category column to a specific item.
        ex: avg_col_perCategory(6, 3, "Autumn Variations")  returns average popularity of songs on the album
    '''
    total = 0
    count = 0
    lst = []
    for row in data[1:]:          
        if row[catCol] == str(filter):   # filters to only item of interest
            lst.append(row)          
    for row in lst:                      # averages column
        total += float(row[datCol])
        count += 1
    return total / count

def avg_col_perAlbum(col, album): 
    ''' 
    Given a column of interest, returns an average of said column only for a specified album.
    '''
    total = 0
    count = 0
    lst = []
    for row in data[1:]:         # filters column
        if row[3] == album:
            lst.append(row)
    for row in lst:              # averages column
        total += float(row[col])
        count += 1
    return total / count

def avg_col_byAlbum(col):    
    ''' 
    Given a column of interest, returns a list of tuples with the average of that column, 
    which is calculated using the function avg_col_perAlbum() and create_dict().
    '''
    albums = list(create_dict(3).items())
    lst = []
    for (key, val) in albums:                             # creates a sorted list of tuples 
        lst.append((avg_col_perAlbum(col,key),key))       # with column averages on the left, 
    lst.sort(reverse=True)                                # sorted in descending order,
    return lst                                            # and album names on the right.                

def avg_col_byYear(col):
    '''
    Given a column. Averages the column for each year and returns a list of tuples of the average 
    of that column and the associated year.
    '''
    years = list(create_dict(23).items())
    lst = []
    for (year, tally) in years:                                  # creates a sorted list of tuples 
        lst.append((avg_col_perCategory(col, 23, year),year))    # with column averages on the left, 
    lst.sort(reverse=True)                                       # sorted in descending order,
    return lst                                                   # and album names on the right. 

# Questions
print("1. What are Ed Sheeran's top 3 most danceable releases averaged by album?")

print("Ed Sheeran's top 3 most danceable releases are " + avg_col_byAlbum(8)[0][1] +  
      ", " + avg_col_byAlbum(8)[1][1] + ", and " + avg_col_byAlbum(8)[2][1] + ".\n")

print("2. What are the top 3 quietest releases averaged by album?")

print("Ed Sheeran's top 3 quietest releases are " + avg_col_byAlbum(11)[-1][1] +
      ", " + avg_col_byAlbum(11)[-2][1] + ", and " + avg_col_byAlbum(11)[-3][1] + ".\n")

print("3. What are the top 3 years where he had the most popular releases on average?")

print("Ed Sheeran's top 3 years where he had the most popular releases on average are", 
      avg_col_byYear(6)[0][1] + ", " + avg_col_byYear(6)[1][1] + ", " + avg_col_byYear(6)[2][1] + ".\n")


### TESTING

# 18 = tempo
#print(avg_col_byAlbum(18)[0][1] +  ", " + avg_col_byAlbum(18)[1][1] + ", and " + avg_col_byAlbum(18)[2][1] + ".\n")

#print(avg_col_byYear(18)[0][1] + ", " + avg_col_byYear(18)[1][1] + ", " + avg_col_byYear(18)[2][1] + ".\n")

# 9 = energy
#print(avg_col_byAlbum(9)[0][1] +  ", " + avg_col_byAlbum(9)[1][1] + ", and " + avg_col_byAlbum(9)[2][1] + ".\n")

#print(avg_col_byYear(9)[0][1] + ", " + avg_col_byYear(9)[1][1] + ", " + avg_col_byYear(9)[2][1] + ".\n")