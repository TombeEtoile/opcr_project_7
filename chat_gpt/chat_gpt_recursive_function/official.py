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

# Convertir les pourcentages de bénéfice en valeurs absolues pour faciliter le calcul
for action, details in actions.items():
    cost = details['coût par action']
    benefit_percent = float(details['bénéfice'].strip('%')) / 100
    details['bénéfice absolu'] = cost * benefit_percent


def bruteforce(index=0, current_cost=0, current_benefit=0, included_actions=[]):

    # Si le coût dépasse le budget, retourner un bénéfice nul pour cette combinaison
    if current_cost > 500:
        return 0, []

    # Si tous les articles ont été considérés, retourner le bénéfice accumulé
    if index >= len(actions):
        # print(included_actions)
        return current_benefit, included_actions

    # Obtenir le nom de l'action actuelle
    action_name = f"Action-{index + 1}"
    action_details = actions[action_name]
    # print(action_details)
    cost = action_details['coût par action']
    benefit = action_details['bénéfice absolu']

    # Option 1: Ne pas inclure l'action actuelle
    without_this, actions_without = bruteforce(index + 1, current_cost, current_benefit, included_actions)

    # Option 2: Inclure l'action actuelle si cela ne dépasse pas le budget
    with_this, actions_with = bruteforce(index + 1, current_cost + cost, current_benefit + benefit,
                                         included_actions + [action_name])

    # Choisir l'option qui maximise le bénéfice
    if with_this > without_this:
        return with_this, actions_with
    else:
        return without_this, actions_without

# Affichage final
best_benefit, best_combination = bruteforce()
print("Meilleur bénéfice :", best_benefit)
print("Combinaison d'actions :", best_combination)
total_test = []
for action in best_combination:
    test = actions[action]['coût par action']
    total_test.append(test)
total_cost = sum(total_test)
print("Coût total :", total_cost, "€")
