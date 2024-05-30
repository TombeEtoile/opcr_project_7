actions = {
    "Action-1": {"coût par action": 20, "bénéfice": "5%"},
    "Action-2": {"coût par action": 30, "bénéfice": "10%"},
    "Action-3": {"coût par action": 50, "bénéfice": "15%"},
    "Action-4": {"coût par action": 70, "bénéfice": "20%"},
    "Action-5": {"coût par action": 60, "bénéfice": "17%"},
    "Action-6": {"coût par action": 80, "bénéfice": "25%"},
    "Action-7": {"coût par action": 22, "bénéfice": "7%"},
    "Action-8": {"coût par action": 26, "bénéfice": "11%"},
    "Action-9": {"coût par action": 48, "bénéfice": "13%"},
    "Action-10": {"coût par action": 34, "bénéfice": "27%"},
    "Action-11": {"coût par action": 42, "bénéfice": "17%"},
    "Action-12": {"coût par action": 110, "bénéfice": "9%"},
    "Action-13": {"coût par action": 38, "bénéfice": "23%"},
    "Action-14": {"coût par action": 14, "bénéfice": "1%"},
    "Action-15": {"coût par action": 18, "bénéfice": "3%"},
    "Action-16": {"coût par action": 8, "bénéfice": "8%"},
    "Action-17": {"coût par action": 4, "bénéfice": "12%"},
    "Action-18": {"coût par action": 10, "bénéfice": "14%"},
    "Action-19": {"coût par action": 24, "bénéfice": "21%"},
    "Action-20": {"coût par action": 114, "bénéfice": "18%"}
}

budget = 500

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
            print(best_benefit[a])

final_max_benefit = max(best_benefit)
max_index = best_benefit.index(final_max_benefit)
final_max_actions = best_actions[max_index]

total_cost = []
for name in final_max_actions:
    total_cost.append(actions[name]['coût par action'])

print("Le benefice maximal réalisable est de",
      final_max_benefit,
      "€ pour un budget total de",
      sum(total_cost),
      "€.\n"
      "Ce bénéfice est réalisable via l'achat du groupement d'actions suivant :\n",
      final_max_actions)

