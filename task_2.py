# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.
with open('task_2_file.txt') as f_obj:
    read_file = f_obj.readlines()

print(f'Количество строк: {len(read_file)}')

for n, word in enumerate(read_file, 1):
    print(f'Количество слов в строке {n}: {len(word.split())}')  # строку в list и считаем кол-во элементов в нём
