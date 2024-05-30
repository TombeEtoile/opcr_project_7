import csv

all_actions = []
scale_factor = 100

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
    all_actions = (all_tuples[i][0],
                   int(float(all_tuples[i][1]) * 100),
                   float(all_tuples[i][1]) * (float(all_tuples[i][2]) / 100))
    all_good_tuples.append(all_actions)


def backpack_algo(budget, actions, scale_factor):
    scaled_budget = int(budget * scale_factor)

    wallet = [[0 for _ in range(scaled_budget + 1)] for _ in range(len(actions) + 1)]

    for a in range(1, len(actions) + 1):
        for b in range(1, scaled_budget + 1):
            if actions[a-1][1] <= b:
                wallet[a][b] = max(actions[a-1][2] + wallet[a-1][b - actions[a-1][1]], wallet[a-1][b])
            else:
                wallet[a][b] = wallet[a-1][b]

    b = scaled_budget
    a = len(actions)
    selected_actions = []

    while b > 0 and a > 0:
        action_parsed = actions[a - 1]
        if b >= action_parsed[1] and wallet[a][b] == wallet[a-1][b - action_parsed[1]] + action_parsed[2]:
            selected_actions.append(action_parsed)
            b -= action_parsed[1]
        a -= 1

    return wallet[-1][-1], selected_actions

print(backpack_algo(budget=170, actions=all_good_tuples, scale_factor=scale_factor))
