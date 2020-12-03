# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

with open('task_4_file_en.txt', encoding='utf-8') as f_obj4_en:
    with open('task_4_file_rus.txt', 'w', encoding='utf-8') as f_obj4_rus:
        for num in f_obj4_en.readlines():
            if num.split()[0] == 'One':
                f_obj4_rus.write(num.replace('One', 'Один'))
            elif num.split()[0] == 'Two':
                f_obj4_rus.write(num.replace('Two', 'Два'))
            elif num.split()[0] == 'Three':
                f_obj4_rus.write(num.replace('Three', 'Три'))
            elif num.split()[0] == 'Four':
                f_obj4_rus.write(num.replace('Four', 'Четыре'))
