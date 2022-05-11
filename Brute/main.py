import itertools
import time
import csv
import os, psutil

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

def input_invest():
    while 1:
        invest_max = input()
        if 0 <= float(invest_max) <= 500:
            return float(invest_max)
        print("response between 0 and 500")


def find_all_combinations(table_actions, invest_max):
    dicts = {}

    for y in range(len(table_actions)):
        try:
            if float(table_actions[y]['price']) > 0 and float(table_actions[y]['price']) < invest_max:
                dicts[table_actions[y]['name']] = float(table_actions[y]['price'])
        except ValueError:
            pass

    list_prices = list(dicts.values())
    combinations = [seq for i in range(len(list_prices), 0, -1)
                    for seq in itertools.combinations(list_prices, i)
                    if sum(seq) < int(invest_max) and sum(seq) > int(invest_max) * 0.80]

    return combinations, dicts

def calc_all_profit(combinations, dicts, table_actions):
    dic_value = {}
    for i in range(len(combinations)):
        list_names = []
        for nb_action in range(len(combinations[i])):
            list_names.append(list(dicts.keys())[list(dicts.values()).index(combinations[i][nb_action])])

        actions = []

        for y in range(len(list_names)):
            result = [(item for item in table_actions if item["name"] == list_names[y])]
            list_result = list(result[0])[0]
            actions.append(list_result)

        price_combination = []
        invoice_combination = []
        for item in range(len(actions)):
            action_invoice = float(actions[item]["price"]) + (float(actions[item]["profit"])/100 * float(actions[item]["price"]))

            price_combination.append(float(actions[item]["price"]))
            invoice_combination.append(action_invoice)

        invoice_combinations = sum(invoice_combination)
        price_combinations = sum(price_combination)

        value = (invoice_combinations/price_combinations) * 100
        dic_value[value] = actions

    sorted_dict = {k: dic_value[k] for k in sorted(dic_value, reverse=True)}
    print(sorted_dict[list(sorted_dict.keys())[0]])

def main():

    process = psutil.Process(os.getpid())
    invest_max = input_invest()
    table_actions = open_data()
    start = time.time()
    combinations, dicts = find_all_combinations(table_actions, invest_max)
    calc_all_profit(combinations, dicts, table_actions)

    end = time.time()
    print("\n" + str(end - start) + " seconds")
    print(str(process.memory_info().rss) + " bytes")


if __name__ == "__main__":
    main()
