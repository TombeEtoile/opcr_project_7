# Créer plusieurs valeur dans un tableau
tab = [3] * 10
# print(tab)

# Créer plusieurs tableaux dans un tableau
tab_in_tab = [[]] * 10
# print(tab_in_tab)

for c in range(5, 3, 10):
    # print(c)
    pass

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

for action, details in actions.items():
    cost = details['coût par action']
    benefit_percent = float(details['bénéfice'].strip('%')) / 100
    details['bénéfice absolu'] = cost * benefit_percent

dp = [0] * 11
picks = [[] for _ in range(11)]

for i, (action_name, details) in enumerate(actions.items()):
    print(f"Examinons {action_name} avec les détails {details}")
    cost = details['coût par action']
    benefit = details['bénéfice absolu']
    print(f"Coût: {cost}, Bénéfice: {benefit}")
    for c in range(10, cost - 1, -1):
        print(f"Vérification du coût: {c}")
        if dp[c - cost] + benefit > dp[c]:
            print(f"Mise à jour de dp[{c}] de {dp[c]} à {dp[c - cost] + benefit}")
            dp[c] = dp[c - cost] + benefit
            picks[c] = picks[c - cost] + [action_name]
            print(f"Actions menant à ce bénéfice: {picks[c]}")
