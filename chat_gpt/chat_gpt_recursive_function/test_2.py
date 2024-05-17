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
    detail['bénéfice part'] = cost * benefice


def bruteforce2(index=0, all_cost=0, all_benefice=0, actions_keept=[]):

    if all_cost >= 500:
        return 0, []

    if index >= len(actions):
        return all_benefice, actions_keept

    action_name = f"Action-{index + 1}"
    action_details = actions[action_name]
    action_cost = action_details['coût par action']
    action_benefice = action_details['bénéfice part']

    without_this, actions_without = bruteforce2(index + 1,
                                                all_cost,
                                                all_benefice,
                                                actions_keept)
    # print('without_this =', without_this)
    print('actions_without =', actions_without)

    with_this, actions_with = bruteforce2(index + 1,
                                          all_cost + action_cost,
                                          all_benefice + action_benefice,
                                          actions_keept + [action_name])
    # print('with_this =', with_this)
    print('actions_with =', actions_with)

    if with_this > without_this:
        return with_this, actions_with
    else:
        return without_this, actions_without


best_benefit, best_combination = bruteforce2()
print("Le meilleur bénéfice possible est :", best_benefit)
print("La combinaison d'action pour y arriver est :", best_combination)
all_cost = []
for action in best_combination:
    cost = actions[action]['coût par action']
    all_cost.append(cost)
print("Le coût total de cette combinaison est de :", sum(all_cost), "€")
