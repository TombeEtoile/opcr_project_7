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
    benefit = float(detail['bénéfice'].strip('%')) / 100
    detail['benefit part'] = cost * benefit
    print(detail['benefit part'])


def brutforce_test_1(index=0, total_cost=0, total_benefit=0, actions_retained=[]):

    if total_cost > 500:
        actions_retained = 0, []

    if len(actions) >= index:
        # mauvaise logique. = inverse : if index >= len(action) --> return total_benefit, actions_retained
        index += 1
        # FAUX

    # pas de suite = pas la logique


