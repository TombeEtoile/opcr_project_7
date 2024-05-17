"""
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


    action_cost = actions[f'Action-{a}']['coût par action']
    percentage = 1 + (int(actions[f'Action-{a + 1}']['bénéfice'].replace("%", "")) / 100)
    benefice = f"{((action_cost * percentage) - action_cost):.2f}€"
    budget = 500

    def list_action_cost():

    all_action_cost = []

    for a in range(len(actions)):
        action_cost = actions[f'Action-{a + 1}']['coût par action']
        all_action_cost.append(action_cost)
        a += 1

    # print(all_action_cost)
    return all_action_cost

"""

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


budget = input("Entrez votre budget : ")

chaine = str()


def test(chaine, budget):
    if chaine != budget:
        print(f"{chaine} --- budget = {budget}---")
    else:
        print(f"VOUS AVEZ TROUVÉ --- {chaine} ---")


for a in letters:
    chaine = a
    test(chaine, budget)

    for b in letters:
        chaine = a + b
        test(chaine, budget)


"""
def bruteforce(action_cost, total_cost):

    budget = 500

    if total_cost < budget:
        for number in list_action_cost():
            if result <= action_cost + number:
                print(f"Le coût est de {action_cost + number}")
            else:
                print(action_cost + number)
                bruteforce(action_cost + number, total_cost + 1)


list_action_cost()
bruteforce("", 1)
"""
