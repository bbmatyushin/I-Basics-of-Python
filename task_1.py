# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('task_1_file.txt', 'w') as file_txt:
    while True:
        user_write = input('Это будет записано в файл: ')
        file_txt.write(user_write + '\n')
        if not user_write:
            break