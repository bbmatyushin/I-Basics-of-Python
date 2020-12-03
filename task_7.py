# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

with open('task_7_file.txt', encoding='utf-8') as f_obj7:
    file_list = [line.split() for line in f_obj7]
    firms_list = [i[0] for i in file_list]  # соираем лист из фирм
    profit_list = [int(profit[2]) - int(profit[3]) for profit in file_list]  # собираем лист с прибылями
    pos_profit = [n for n in profit_list if n > 0]  # лист только с положительными прибылями
    mean_profit = sum(pos_profit) / len(pos_profit)
    profit_dict = {'average_profit': round(mean_profit, 2)}
    firms_dict = {key: val for key, val in zip(firms_list, profit_list)}  # словарь фирма + её прибыль
    finish_list = []
    finish_list.append(firms_dict)
    finish_list.append(profit_dict)
    print(finish_list)


with open('task_7_file.json', 'w', encoding='utf-8') as f:
    json.dump(finish_list, f)
