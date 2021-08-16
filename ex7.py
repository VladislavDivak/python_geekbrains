import json

with open('ex7_firms.txt', 'r', encoding='utf-8') as r_ex7:
    firms_analysis = {}
    total_profit = 0
    i = 0
    while True:
        firm_data = r_ex7.readline().split(' ')
        place = r_ex7.tell()
        revenue = int(firm_data[2])
        spend = int(firm_data[3].replace('\n', ''))
        profit = revenue - spend
        new_firm = {firm_data[0]: profit}
        firms_analysis.update(new_firm)
        if profit >= 0:
            print(f'Profit of {firm_data[0]} is {profit}')
            total_profit = total_profit + profit
            i += 1
        else:
            print(f'Loss of {firm_data[0]} is {profit}')
        if r_ex7.readline() == '':
            break
        else:
            r_ex7.seek(place)
    average_profit = {'average profit': int(total_profit/i)}
    data_for_json = [firms_analysis, average_profit]

with open("ex7.json", "w") as write_f:
    json.dump(data_for_json, write_f)

