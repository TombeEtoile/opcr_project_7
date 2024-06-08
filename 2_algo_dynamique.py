import csv

all_tuples = []
actions_dict = {}

user_input = input('Which data do you want to analyze?\n'
                   '1 - data 1\n'
                   '2 - data 2\n'
                   'Your answer: ')

with open(f'data/data_{user_input}.csv', newline='') as csvfile:
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

for action, details in actions_dict.items():
    cost = details['coût par action']
    benefit = float(details['bénéfice']) / 100
    details['benefit part'] = cost * benefit

best_benefit = [0] * (budget + 1)
best_actions = [[]] * (budget + 1)

for i, (action, details) in enumerate(actions_dict.items()):
    cost = details['coût par action']
    benefit_part = details['benefit part']
    for a in range(budget, cost - 1, -1):
        if best_benefit[a - cost] + benefit_part > best_benefit[a]:
            best_benefit[a] = best_benefit[a - cost] + benefit_part
            best_actions[a] = best_actions[a - cost] + [action]

final_max_benefit = max(best_benefit)
max_index = best_benefit.index(final_max_benefit)
final_max_actions = best_actions[max_index]

total_cost = []
for name in final_max_actions:
    total_cost.append(actions_dict[name]['coût par action'])

print("Le benefice maximal réalisable est de",
      final_max_benefit / 100,
      "€ pour un budget total de",
      sum(total_cost) / 100,
      "€.\n"
      "Ce bénéfice est réalisable via l'achat du groupement d'actions suivant :\n",
      final_max_actions)
