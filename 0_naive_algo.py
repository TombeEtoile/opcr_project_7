import csv

all_tuples = []
actions_dict = {}

user_input = input('Which data do you want to analyze?\n'
                   '1 - data 1\n'
                   '2 - data 2\n'
                   'Your answer: ')

with open(f'data_{user_input}.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            all_tuples.append((row[0], float(row[1]), float(row[2])))
        except ValueError:
            pass

filtered_tuples = [t for t in all_tuples if t[1] >= 0 and t[2] > 0]

scaled_tuples = [(t[0], int(t[1] * 100), t[2]) for t in filtered_tuples]

scaled_tuples = scaled_tuples[1:]

for t in scaled_tuples:
    actions_dict[t[0]] = {"coût par action": t[1], "bénéfice": t[2]}

budget = 500 * 100
best_actions = []
a = 0

for action, details in actions_dict.items():
    cost = details['coût par action']
    benefit = float(details['bénéfice']) / 100
    details['benefit part'] = cost * benefit
    details['max benefice'] = (budget / cost) * details['benefit part']

sorted_items = sorted(actions_dict.items(), key=lambda item: item[1]['max benefice'], reverse=True)
sorted_actions = dict(sorted_items)

tentative = [[] for _ in range(len(actions_dict))]

possibilities = []
current_combination = []

for action in sorted_actions:
    current_combination.append(action)
    possibilities.append(current_combination[:])

all_cost = []
all_benefice = []

for combinaison in possibilities:
    total_cost = 0
    total_benefice = 0
    for action_name in combinaison:
        total_cost += sorted_actions[action_name]['coût par action']
        total_benefice += sorted_actions[action_name]['benefit part']
    all_cost.append(total_cost)
    all_benefice.append(total_benefice)

final_cost = [0]

for i in range(len(all_cost)):
    if all_cost[i] > budget:
        pass
    elif final_cost[0] < all_cost[i]:
        final_cost[0] = all_cost[i]

index_actions = all_cost.index(final_cost[0])
winner_actions = possibilities[index_actions]
best_benefice = all_benefice[index_actions]

print("Le benefice maximal réalisable est de",
      best_benefice / 100,
      "€ pour un budget total de",
      final_cost[0] / 100,
      "€.\n"
      "Ce bénéfice est réalisable via l'achat du groupement d'actions suivant :\n",
      winner_actions)
