actions = {
    "Action-1": {"coût par action": 20, "bénéfice": "5%"},
    "Action-2": {"coût par action": 30, "bénéfice": "10%"},
    "Action-3": {"coût par action": 50, "bénéfice": "15%"},
    "Action-4": {"coût par action": 70, "bénéfice": "20%"},
    "Action-5": {"coût par action": 60, "bénéfice": "17%"},
    "Action-6": {"coût par action": 80, "bénéfice": "25%"},
}

for action, detail in actions.items():
    cost = detail['coût par action']
    benefice = float(detail['bénéfice'].strip('%')) / 100
    detail['benefice_part'] = cost * benefice


def bruteforce_rec_3(index=0, total_cost=0, total_benefice=0, actions_retain=[]):

    if total_cost > 500:
        return 0, []

    if index >= len(actions):
        return total_benefice, actions_retain

    action_name = f'Action-{index + 1}'
    action_details = actions[action_name]
    action_cost = action_details['coût par action']
    action_benefice = action_details['benefice_part']

    without_in, action_without = bruteforce_rec_3(index + 1, total_cost, total_benefice, actions_retain)

    with_in, action_with = bruteforce_rec_3(index + 1, total_cost + action_cost, total_benefice + action_benefice, actions_retain + [action_name])

    if with_in < without_in:
        return without_in, action_without

    else:
        return with_in, action_with


print(bruteforce_rec_3())
total_benefit, total_actions = bruteforce_rec_3()
print("Le bénéfice total sera de :", total_benefit)
print("La séquence d'actions sur lesquelles investir est :", total_actions)
total_cost = []
for the_action in total_actions:
    total_cost.append(actions[the_action]['coût par action'])
all_total_cost = sum(total_cost)
print("Le coût total de ces achats sera de :", all_total_cost, "€")
