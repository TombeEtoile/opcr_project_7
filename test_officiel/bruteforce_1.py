# Actions à analyser
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

# extraction des information en dur
for action, details in actions.items():
    cost = details['coût par action']
    benefit_percent = float(details['bénéfice'].strip('%')) / 100
    details['benefit_absolu'] = cost * benefit_percent

benefice_tab = [0] * (len(actions) + 1)
action_tab = [[]] * (len(actions) + 1)

for i, (action, details) in enumerate(actions.items()):
    cost = details['coût par action']
    benefice = details['benefit_absolu']

    for a in range(budget, cost - 1, -1):

        if benefice_tab[a - cost] + benefice > benefice_tab[a]:
            print(benefice_tab[a - cost] + benefice)
            print(benefice_tab[a])
            benefice_tab[a] = benefice_tab[a - cost] + benefice
            action_tab[a] = action_tab[action]
