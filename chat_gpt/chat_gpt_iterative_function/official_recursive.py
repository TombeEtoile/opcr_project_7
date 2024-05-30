# Définition des actions
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


def bruteforce_iterative(actions, budget):

    # Convertir les pourcentages de bénéfice en valeurs absolues pour faciliter le calcul
    for action, details in actions.items():
        cost = details['coût par action']
        benefit_percent = float(details['bénéfice'].strip('%')) / 100
        details['bénéfice absolu'] = cost * benefit_percent

    # Créer un tableau pour stocker les bénéfices maximaux à chaque niveau de coût
    dp = [0] * (budget + 1)  # dp[c] représente le bénéfice maximum pour un coût c

    # Table pour suivre les actions choisies pour chaque budget
    picks = [[]] * (budget + 1)

    # Remplir le tableau en considérant chaque action
    for i, (action_name, details) in enumerate(actions.items()):
        print(i + 1, (action_name, details))
        cost = details['coût par action']
        benefit = details['bénéfice absolu']

        # Mettre à jour le tableau dp du haut vers le bas pour éviter de compter une action plusieurs fois
        for c in range(budget, cost - 1, -1):
            if dp[c - cost] + benefit > dp[c]:
                dp[c] = dp[c - cost] + benefit
                picks[c] = picks[c - cost] + [action_name]
                print(f'{i + 1} : cost = {c}\npicks[{c}] --> {picks[c]} \ndp[{c}] --> {dp[c]} ')

    print(dp)

    # Trouver le bénéfice maximal possible et les actions correspondantes
    max_benefit = max(dp)
    max_index = dp.index(max_benefit)
    best_combination = picks[max_index]

    return max_benefit, best_combination


# Appel de la fonction
budget = 10
best_benefit, best_combination = bruteforce_iterative(actions, budget)
print("Meilleur bénéfice:", best_benefit)
print("Combinaison d'actions:", best_combination)
