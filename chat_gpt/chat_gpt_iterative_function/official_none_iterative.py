# Définition des actions
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


def bruteforce_iterative(actions, budget):

    # Nombre d'actions
    n = len(actions)

    # Convertir les pourcentages de bénéfice en valeurs absolues pour faciliter le calcul
    for action, details in actions.items():
        cost = details['coût par action']
        benefit_percent = float(details['bénéfice'].strip('%')) / 100
        details['bénéfice absolu'] = cost * benefit_percent

    # Créer un tableau pour stocker les bénéfices maximaux à chaque niveau de coût
    dp = [0] * (budget + 1)  # dp[c] représente le bénéfice maximum pour un coût c

    # Table pour suivre les actions choisies pour chaque budget
    picks = [[] for _ in range(budget + 1)]

    # Remplir le tableau en considérant chaque action
    for i, (action_name, details) in enumerate(actions.items()):
        print(i, (action_name, details))
        cost = details['coût par action']
        benefit = details['bénéfice absolu']
        # Mettre à jour le tableau dp du haut vers le bas pour éviter de compter une action plusieurs fois
        for c in range(budget, cost - 1, -1):
            if dp[c - cost] + benefit > dp[c]:
                dp[c] = dp[c - cost] + benefit
                picks[c] = picks[c - cost] + [action_name]

    # Trouver le bénéfice maximal possible et les actions correspondantes
    max_benefit = max(dp)
    max_index = dp.index(max_benefit)
    best_combination = picks[max_index]

    return max_benefit, best_combination


# Appel de la fonction
budget = 500
best_benefit, best_combination = bruteforce_iterative(actions, budget)
print("Meilleur bénéfice:", best_benefit)
print("Combinaison d'actions:", best_combination)
