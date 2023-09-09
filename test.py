import csv

file = "agents_position4200.csv"


fields = []
rows = []

final = []

with open(file, 'r') as csvfile: 

    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader: 
        rows.append(row) 
# printing the field names
 
# printing first 5 rows
for row in rows:
    # parsing each column of a row
    count = 0
    print(row)
    for col in row[0:10]:
        if(count == 5):
            test = col[col.index('(')+1:col.index(')')].split()
            test[0] = float(test[0])
            test[1] = float(test[1])
            final.append(test)
            count = 0
        count+=1
