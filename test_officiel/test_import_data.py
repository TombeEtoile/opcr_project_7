import csv

all_tuples = []

# Lire les données du CSV et les convertir en tuples
with open('../data/data_2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            all_tuples.append((row[0], float(row[1]), float(row[2])))
        except ValueError:
            pass

filtered_tuples = [t for t in all_tuples if t[1] >= 0]

filtered_tuples = [t for t in filtered_tuples if t[2] > 0]

filtered_tuples = filtered_tuples[1:]

