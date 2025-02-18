import csv
data = list(csv.reader(open(college_hs_wages.csv)))
hs_wages = get_hs_wages(data)

def get_hs_wages(all_data):
    wages = []
    for row in range(1,len(all_data)):
        wages.append(row[1])
    return wages