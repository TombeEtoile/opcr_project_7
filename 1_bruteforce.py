import csv
from itertools import combinations
import time


def load_data(user_input):

    all_tuples = []
    actions_dict = {}

    with open(f'data/data_{user_input}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                all_tuples.append((row[0], float(row[1]), float(row[2])))
            except ValueError:
                pass

    filtered_tuples = [t for t in all_tuples if t[1] >= 0 and t[2] > 0]

    filtered_tuples = filtered_tuples[1:]

    for t in filtered_tuples:
        actions_dict[t[0]] = {"coût par action": t[1], "bénéfice": t[2]}

    return actions_dict


def bruteforce(actions, budget):
    best_benefit = 0
    best_combination = []

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions.items(), r):
            total_cost = sum(action[1]['coût par action'] for action in combination)
            if total_cost <= budget:
                total_benefit = sum(action[1]['bénéfice'] for action in combination)
                if total_benefit > best_benefit:
                    best_benefit = total_benefit
                    best_combination = combination

    return best_benefit, best_combination


def main():

    user_input = input('Which data do you want to analyze?\n'
                       '1 - data 1\n'
                       '2 - data 2\n'
                       'Your answer: ')

    start_time = time.time()

    actions_dict = load_data(user_input)

    best_benefit, best_combination = bruteforce(actions=actions_dict, budget=500)

    end_time = time.time()
    execution_time = end_time - start_time

    total_cost = sum(action[1]['coût par action'] for action in best_combination)

    print("Le bénéfice maximal réalisable est de",
          best_benefit,
          "€ pour un budget total de",
          total_cost,
          "€.\n"
          "Ce bénéfice est réalisable via l'achat du groupement d'actions suivant :\n",
          [action[0] for action in best_combination])
    print("Temps d'exécution :", execution_time)


if __name__ == '__main__':
    main()
