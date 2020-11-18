# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input('Введите число от 1 до 9: '))
sum = user_number + user_number * 11 + user_number * 111
print(f'{user_number} + {user_number}{user_number} + {user_number}{user_number}{user_number} = {sum}')
