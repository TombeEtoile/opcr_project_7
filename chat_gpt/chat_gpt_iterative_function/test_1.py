def bruteforce_iterative():

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
    all_scenarios = []

    for action, details in actions.items():
        cost = details['coût par action']
        benefit = float(details['bénéfice'].strip('%')) / 100
        details['action_benefit'] = cost * benefit
        # print(f"cost = {cost}")
        # print(f"benefit = {benefit}")
        # print(f"details['action_benefit'] = {details['action_benefit']}")

    # for x in range(len(actions) * len(actions)):



bruteforce_iterative()

"""
le but :
créer un dictionnaire all_scénarios = []
pour len(actions) * len(actions) = 400 --> créer 400 dictionnaires vides
pour len(nombre de dictionnaires vides) = 400 --> ajouter (exemple pour 3 actions) :
[A1]
[A1, A2]
[A1, A3]
[A1, A2, A3]
[A2]
[A2, A3]
[A3]
Checker pour chaque dictionnaire le budget & le benefice
"""
