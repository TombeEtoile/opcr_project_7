
actions = {
    "Action-1": {"coût par action": 20, "bénéfice": "5%"},
    "Action-2": {"coût par action": 30, "bénéfice": "10%"},
    "Action-3": {"coût par action": 50, "bénéfice": "15%"},
    "Action-4": {"coût par action": 70, "bénéfice": "20%"},
    "Action-5": {"coût par action": 60, "bénéfice": "17%"},
}


all_actions = []

for action, details in actions.items():
    cost = details['coût par action']
    benefit = float(details['bénéfice'].strip('%')) / 100
    details['action_benefit'] = cost * benefit
    # print(f"cost = {cost}")
    # print(f"benefit = {benefit}")
    # print(f"details['action_benefit'] = {details['action_benefit']}")

all_scenarios = [[]] * len(actions) * len(actions)

for a in range(len(actions)):
    action_name = f"Action-{a + 1}"
    all_actions.append(action_name)

for a in range(5):
    all_scenarios[a].append(actions[f'Action-{a + 1}'])


print(all_scenarios)


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
