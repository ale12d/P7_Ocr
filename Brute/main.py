import itertools

def main():
    while 1:
        while 1:
            invest = input()
            if 0 <= int(invest) <= 500:
                break
            print("n")

        action_benef = {20:5,30:10,50:15,70:20,60:17,80:25,4:7,26:11,48:13,34:27,42:17}
        list_benef_total= []
        invest_benef_pourcent = {}
        invest_benef_euro = {}
        result_invest_total = []

        result = [seq for i in range(len(action_benef), 0, -1)
                  for seq in itertools.combinations(action_benef.keys(), i)
                  if sum(seq) < int(invest)]

        for i in range(len(result)):
            result_invest_total.append(sum(result[i]))

        for nb_combination in range(len(result)):
            list_benef_euro =[]
            for nb_action in range(len(result[nb_combination])):
                benef_pourcent = action_benef[result[nb_combination][nb_action]]
                cout_action = result[nb_combination][nb_action]
                benef_euro = cout_action*(benef_pourcent/100)
                list_benef_euro.append(benef_euro)
                benef_euro_total = sum(list_benef_euro)


            benef_pourcent_total = benef_euro_total/result_invest_total[nb_combination]
            list_benef_total.append(result_invest_total[nb_combination]+benef_pourcent_total*result_invest_total[nb_combination])

            invest_benef_euro[result_invest_total[nb_combination] + benef_euro_total] = result[nb_combination]
            invest_benef_pourcent[benef_pourcent_total] = result[nb_combination]
            list_benef_total.sort(reverse=True)

        print("-----------")

        for key, value in invest_benef_pourcent.items():
            if invest_benef_euro[list_benef_total[0]] == value:
                print("argent de depart : " + str(round(list_benef_total[0]/(1+key), 1)) + "$")
                print("argent attendu : " + str(list_benef_total[0]) + " $")
                print("benef : " + str(round(key*100,2)) + "%")
                print("cout des actions individuelement : " + str(invest_benef_euro[list_benef_total[0]]))



if __name__ == "__main__" :
    main()