# 6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.

quantity_goods = int(input('Сколько всего товаров: '))
goods = []
goods_dict = {}

for el in range(quantity_goods):
    num = el + 1
    title = input('Введите название товара: ')
    price = int(input('Укажите стоимость: '))
    quantity = int(input('Укажите количество: '))
    unit = input('Укажите единицу измерения: ')
    goods_dict['название'] = title
    goods_dict['цена'] = price
    goods_dict['количество'] = quantity
    goods_dict['ед.'] = unit
    structure = num, goods_dict  # номер товара и словарь с параметрами
    goods.append(structure)

print(goods)

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров

# goods_list = [(1, {'название': 'Товар 1', 'цена': 50, 'количество': 2, 'ед.': 'шт'}),
#               (2, {'название': 'Товар 2', 'цена': 100, 'количество': 6, 'ед.': 'шт'})]
# my_list = []
# d1 = goods_list[0][1]
# my_list.append(d1['название'])
# d2 = goods_list[1][1]
# my_list.append(d2['название'])
# result = dict(название=list(set(my_list)))  # удаляем дубликаты в списке, если есть.
#
# print(result)

# Не успел разобраться как всё собрать в приветси к тому, что на примере.
