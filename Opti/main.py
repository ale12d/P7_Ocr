import csv
import os
import psutil
import time


def input_invest():
    while 1:
        invest_max = input()
        if 0 <= float(invest_max) <= 500:
            return float(invest_max)
        print("response between 0 and 500")


def open_data():
    file1, file2 = open('dataset1_Python+P7.csv'), open('dataset2_Python+P7.csv')
    reader, reader2 = csv.reader(file1), csv.reader(file2)
    table_actions = []

    for row in reader:
        table_action = {"name": row[0], "price": row[1], "profit": row[2]}
        table_actions.append(table_action)

    for row in reader2:
        table_action = {"name": row[0], "price": row[1], "profit": row[2]}
        table_actions.append(table_action)

    return table_actions


def price(action):
    try:
        return float(action['price'])
    except ValueError:
        return 0


def profit(action):
    try:
        return float(action['profit'])
    except ValueError:
        return 0


def algo(table_actions, invest_max):
    sorted_table = sorted(table_actions, key=profit, reverse=True)
    solution = []
    total_invest = 0

    i = 0

    while i < len(sorted_table) and total_invest < invest_max:
        action = sorted_table[i]
        action_price = price(action)

        if total_invest + action_price <= invest_max and action_price > 0.0:
            solution.append(action)
            total_invest = total_invest + action_price

        i = i + 1
    return solution


def print_solution(solution):
    actions_prices = []
    actions_income = []
    for nb_action in range(len(solution)):
        print(
            solution[nb_action]['name'] + " : " + solution[nb_action]['price'] + " $" + " --> " + solution[nb_action][
                'profit'] + " %")
        actions_prices.append(float(solution[nb_action]['price']))

        actions_income.append(float(solution[nb_action]['price']) + (
                    (float(solution[nb_action]['profit']) / 100) * float(solution[nb_action]['price'])))

    invest = sum(actions_prices)
    income = sum(actions_income)
    profit_total = (income / invest) * 100

    print("\n invest : " + str(round(invest, 2)) + " $")
    print(" income : " + str(round(income, 2)) + " $")
    print(" profit : " + "+" + str(round(profit_total - 100, 2)) + " %")
    print("\n------")


def main():
    process = psutil.Process(os.getpid())

    invest_max = input_invest()
    start = time.time()
    table_actions = open_data()
    solution = algo(table_actions, invest_max)

    end = time.time()

    print_solution(solution)

    print("\n" + str(end - start) + " seconds")
    print(str(process.memory_info().rss) + " bytes")


if __name__ == "__main__":
    main()
