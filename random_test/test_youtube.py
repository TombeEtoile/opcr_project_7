actions = {
    "Action-1": {"coût par action": 20.2, "bénéfice": "12.25%"},
    "Action-2": {"coût par action": 30.33, "bénéfice": "38.06%"},
    "Action-3": {"coût par action": 50.13, "bénéfice": "27.69%"},
    "Action-4": {"coût par action": 70.57, "bénéfice": "38.21%"},
    "Action-5": {"coût par action": 60.80, "bénéfice": "27.47%"}
}

all_actions = []

for action, details in actions.items():
    cost = int(details['coût par action'] * 100)  # Mettre à l'échelle par 100
    benefice = float(details['bénéfice'].strip('%')) / 100
    details['benefice_part'] = cost * benefice / 100  # Ajuster pour correspondre à l'échelle
    action_tuple = (action, cost, details['benefice_part'])
    all_actions.append(action_tuple)


def backpack_algo(budget, actions):

    scaled_budget = int(budget * 100)  # Mettre à l'échelle par 100

    wallet = [[0 for _ in range(scaled_budget + 1)] for _ in range(len(actions) + 1)]

    for a in range(1, len(actions) + 1):
        for b in range(1, scaled_budget + 1):
            if actions[a-1][1] <= b:
                wallet[a][b] = max(actions[a-1][2] + wallet[a-1][b - actions[a-1][1]], wallet[a-1][b])
            else:
                wallet[a][b] = wallet[a-1][b]

    b = scaled_budget
    a = len(actions)
    selected_actions = []

    while b >= 0 and a >= 0:
        action_parsed = actions[a - 1]
        if b >= action_parsed[1] and wallet[a][b] == wallet[a-1][b - action_parsed[1]] + action_parsed[2]:
            selected_actions.append(action_parsed)
            b -= action_parsed[1]

        a -= 1

    return wallet[-1][-1], selected_actions


print(backpack_algo(budget=170, actions=all_actions))
