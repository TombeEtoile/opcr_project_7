actions = {
    "Action-1": {"coût par action": 20, "bénéfice": "5%"},
    "Action-2": {"coût par action": 30, "bénéfice": "10%"},
    "Action-3": {"coût par action": 50, "bénéfice": "15%"},
    "Action-4": {"coût par action": 70, "bénéfice": "20%"},
    "Action-5": {"coût par action": 60, "bénéfice": "17%"},
    "Action-6": {"coût par action": 80, "bénéfice": "25%"},
}

for action, details in actions.items():
    cost = details['coût par action']
    benefice = float(details['bénéfice'].strip('%')) / 100
    details['benefice_part'] = cost * benefice


def bruteforce_rec_4(index=0, all_cost=0, all_benefice=0, actions_keept=[]):

    budget = 500

    if all_cost > budget:
        return 0, []

    if index >= len(actions):
        return all_benefice, actions_keept

    action_name = f'Action-{index + 1}'
    action_cost = actions[action_name]['coût par action']
    action_benefice_part = actions[action_name]['benefice_part']

    without_in, action_without = bruteforce_rec_4(index + 1,
                                                  all_cost,
                                                  all_benefice,
                                                  actions_keept)

    with_in, action_with = bruteforce_rec_4(index + 1,
                                            all_cost + action_cost,
                                            all_benefice + action_benefice_part,
                                            actions_keept + [action_name])

    if with_in < without_in:
        return without_in, action_without

    else:
        return with_in, action_with


print(bruteforce_rec_4())
total_benefice, total_actions = bruteforce_rec_4()
print("Le bénéfice total sera de :", total_benefice, "€")
print("Les actions sur lesquelles investir sont :", total_actions)

all_actions = []
for investment in total_actions:
    all_actions.append(actions[investment]['coût par action'])
all_actions_to_invest = sum(all_actions)

print("Le coût total de cet investissement sera de :", all_actions_to_invest, "€")

