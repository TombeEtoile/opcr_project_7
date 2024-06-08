import csv
import time


def load_data(user_input):
    all_tuples = []
    with open(f'data/data_{user_input}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                all_tuples.append((row[0], float(row[1]), float(row[2])))
            except ValueError:
                pass

    filtered_tuples = [t for t in all_tuples if t[1] >= 0 and t[2] > 0]
    scaled_tuples = [(t[0], int(t[1] * 100), t[2]) for t in filtered_tuples]
    scaled_tuples = scaled_tuples[1:]
    return scaled_tuples


def backpack_algo(budget, actions):
    scaled_budget = int(budget * 100)
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
        if wallet[a][b] == wallet[a-1][b - action_parsed[1]] + action_parsed[2]:
            selected_actions.append(action_parsed)
            b -= action_parsed[1]
        a -= 1

    return wallet[-1][-1], selected_actions


def main():
    user_input = input('Which data do you want to analyze?\n'
                       '1 - data 1\n'
                       '2 - data 2\n'
                       'Your answer: ')
    scaled_tuples = load_data(user_input)

    start_time = time.time()

    answer = backpack_algo(budget=500, actions=scaled_tuples)

    end_time = time.time()
    execution_time = end_time - start_time

    gain = answer[0]
    selectionned_actions = []
    all_prices = []
    for action in answer[1]:
        selectionned_actions.append(action[0])
        all_prices.append(action[1] / 100)
    final_price = sum(all_prices)

    print("Actions sélectionnées :", selectionned_actions,
          "\nSoit un total de", len(selectionned_actions), " actions."
          "\nCoût total de l'opération :", final_price, "€",
          "\nGains estimés :", gain, "€")
    print("Temps d'exécution du programme :", execution_time, "secondes")


if __name__ == '__main__':
    main()
