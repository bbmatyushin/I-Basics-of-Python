# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division_func(val1, val2):
    try:
        return val1 / val2
    except ZeroDivisionError:
        return 'Деление на ноль.'


user_num_1 = int(input('Введите числитель: '))
user_num_2 = int(input('Введите знаменатель: '))


print(f'Результат: {division_func(user_num_1, user_num_2)}')