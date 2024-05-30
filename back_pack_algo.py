actions = {
    "Action-1": {"coût par action": 20, "bénéfice": "5%"},
    "Action-2": {"coût par action": 30, "bénéfice": "10%"},
    "Action-3": {"coût par action": 50, "bénéfice": "15%"},
    "Action-4": {"coût par action": 70, "bénéfice": "20%"},
    "Action-5": {"coût par action": 60, "bénéfice": "17%"}
}

all_actions = []

for action, details in actions.items():
    cost = details['coût par action']
    benefice = float(details['bénéfice'].strip('%')) / 100
    details['benefice_part'] = cost * benefice
    action_tuple = (action, details['coût par action'], details['benefice_part'])
    all_actions.append(action_tuple)

# print(all_actions)


def backpack_algo(budget, actions):

    wallet = [[0 for _ in range(budget + 1)] for _ in range(len(actions) + 1)]

    for a in range(1, len(actions) + 1):
        for b in range(1, budget + 1):
            if actions[a-1][1] <= b:
                wallet[a][b] = max(actions[a-1][2] + wallet[a-1][b - actions[a-1][1]], wallet[a-1][b])
            else:
                wallet[a][b] = wallet[a-1][b]

    b = budget
    a = len(actions)
    selected_actions = []

    while b >= 0 and a >= 0:
        action_parsed = actions[a - 1]
        if wallet[a][b] == wallet[a-1][b - action_parsed[1]] + action_parsed[2]:
            selected_actions.append(action_parsed)
            b -= action_parsed[1]

        a -= 1

    return wallet[-1][-1], selected_actions


print(backpack_algo(budget=170, actions=all_actions))
