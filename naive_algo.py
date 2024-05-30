actions = {
    "Action-1": {"coût par action": 20, "bénéfice": "5%"},
    "Action-2": {"coût par action": 30, "bénéfice": "10%"},
    "Action-3": {"coût par action": 50, "bénéfice": "15%"},
    "Action-4": {"coût par action": 70, "bénéfice": "20%"},
    "Action-5": {"coût par action": 60, "bénéfice": "17%"}
}

budget = 200
best_actions = []
a = 0

for action, details in actions.items():
    cost = details['coût par action']
    benefit = float(details['bénéfice'].strip('%')) / 100
    details['benefit part'] = cost * benefit
    details['max benefice'] = (budget / cost) * details['benefit part']
    print(details['benefit part'])

sorted_items = sorted(actions.items(), key=lambda item: item[1]['max benefice'], reverse=True)
sorted_actions = dict(sorted_items)
print(sorted_actions)
print('\n')


tentative = [[] for _ in range(len(actions))]

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
    all_cost.append(total_cost)  # [70, 130, 180, 210, 230]
    all_benefice.append(total_benefice)  # [14.0, 24.200000000000003, 31.700000000000003, 34.7, 35.7]

final_cost = [0]  # 0

for i in range(len(all_cost)):
    if all_cost[i] > budget:
        pass
    elif final_cost[0] < all_cost[i]:
        final_cost[0] = all_cost[i]

index_actions = all_cost.index(final_cost[0])
winner_actions = possibilities[index_actions]
best_benefice = all_benefice[index_actions]

print("Le benefice maximal réalisable est de",
      best_benefice,
      "€ pour un budget total de",
      final_cost[0],
      "€.\n"
      "Ce bénéfice est réalisable via l'achat du groupement d'actions suivant :\n",
      winner_actions)
