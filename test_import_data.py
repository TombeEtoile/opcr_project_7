import csv

actions = []
all_tuples = []
all_good_tuples = []

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        action_tuple = (row[0], row[1], row[2])
        all_tuples.append(action_tuple)
all_tuples.remove(all_tuples[0])

for i in range(len(all_tuples)):
    all_actions = (all_tuples[i][0], int(float(all_tuples[i][1]) * 100), float(all_tuples[i][2]))
    all_good_tuples.append(all_actions)

print(all_good_tuples)


# print(', '.join(row))
