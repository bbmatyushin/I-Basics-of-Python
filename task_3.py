# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.

with open('task_3_file.txt', encoding='utf-8') as f_obj:
    read_file = f_obj.readlines()

print(f'Salary less than 20000: '
      f'{[salary.split()[0] for salary in read_file if float(salary.split()[1]) < 20000]}')

salary_list = [float(salary.split()[1]) for salary in read_file]
print(f'Middle salary: {sum(salary_list) / len(salary_list):.2f}')
