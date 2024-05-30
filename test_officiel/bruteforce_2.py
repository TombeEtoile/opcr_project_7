actions = {
    "Action-1": {"coût par action": 1, "bénéfice": "5%"},
    "Action-2": {"coût par action": 2, "bénéfice": "10%"},
    "Action-3": {"coût par action": 1, "bénéfice": "15%"},
    "Action-4": {"coût par action": 2, "bénéfice": "20%"},
    "Action-5": {"coût par action": 3, "bénéfice": "17%"},
    "Action-6": {"coût par action": 4, "bénéfice": "25%"},
    "Action-7": {"coût par action": 2, "bénéfice": "7%"},
    "Action-8": {"coût par action": 1, "bénéfice": "11%"},
}

budget = 10

for action, details in actions.items():
    cost = details['coût par action']
    benefit = float(details['bénéfice'].strip('%')) / 100
    details['benefit part'] = cost * benefit

best_benefit = [0] * (budget + 1)
best_actions = [[]] * (budget + 1)

for i, (action, details) in enumerate(actions.items()):
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
    total_cost.append(actions[name]['coût par action'])

print("Le benefice maximal réalisable est de",
      final_max_benefit,
      "€, réalisable via l'achat du groupement d'actions suivant :",
      final_max_actions,
      "pour un budget total de",
      sum(total_cost),
      "€.")

