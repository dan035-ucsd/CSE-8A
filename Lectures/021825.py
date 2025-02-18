import csv
data = list(csv.reader(open("college_hs_wages.csv")))


def get_col_data(all_data,col_num):
    targetData = []
    for row in range(1,len(all_data)):
        targetData.append(all_data[row][col_num])
    return targetData

def group_by_rating(song_data):
    grouped_songs = {}
    for song in song_data:
        rating = song[2]
        if rating in grouped_songs:
            grouped_songs[rating].append(song[1])
        else:
            grouped_songs[rating] = [song[1]]
    return grouped_songs

song_data = [['Movie', 'Song Name', 'Rating'], 
             ['Aladdin', 'Friend Like Me', '8'], 
             ['Beauty and the Beast', ' Gaston', '2'],  
             ['Moana', "How Far I'll Go", '8'],
             ['The Little Mermaid', 'Under the Sea', '8'],
             ['The Lion King', 'Circle of Life', '2']]

grouped_songs = group_by_rating(song_data[1:])
print(grouped_songs)

