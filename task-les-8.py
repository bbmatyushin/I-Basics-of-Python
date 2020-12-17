#Loto game with PC
import random
from sys import exit

class LotoCard:
    def __init__(self, name):
        self.name = name
        self.card = self.card_generator()

    def card_generator(self):
        all_nums = [x for x in range(1, 90)]  # генерируем список всех чисел
        nums = random.sample(all_nums, 15)  # выбираем 15 чисел, которые будут на карточке
        for num in nums:
            all_nums.remove(num)  # исключаем выбранные цифры из списка чтобы не попадались вновь
        card = []  # пустая карта в которую потом будет добавляться 3 линии

        for i in range(3):
            line = ['  ' for x in range(1, 10)]  # генерируем пустую линию
            line_nums = nums[i * 5:i * 5 + 5]  # выбираем 5 чисел для данной линии (от 1 до 5; потом от 6 до 10; потом от 11 до 15)
            line_nums.sort()  # сортируем по возрастанию

            line_index = random.sample(range(1, 10), 5)  # генерируем случайную позицию для числа в линии
            line_index.sort()  # сортируем по возрастанию

            i = 0
            for n in line_index:
                line[n-1] = line_nums[i]  # заполняем пустую линию числами в вбранной позиции
                i += 1

            for num in line:
                card.append(num)
        return card

    def card_update(self, num):
        for n, i in enumerate(self.card):
            if i == num:
                self.card[n] = ' - '
        return self.card

    def checking_number(self, num):
        if num in self.card:
            return 'Yes'
        else:
            return 'No'

    def final(self):
        end_game = 0
        for item in self.card:
            if str(item).isdigit():
                end_game += 1
            else:
                pass
        return end_game

    def __str__(self):
        dash = '-' * len(self.card) * 2
        line1 = str(self.card[0:9]) + '\n'
        line2 = str(self.card[9:18]) + '\n'
        line3 = str(self.card[18:28]) + '\n'
        return f'{self.name}:\n {dash}\n {line1} {line2} {line3} {dash}'

def bochonok():
    bochonok = random.sample(meshok, 1)  # выбираем 15 чисел, которые будут на карточке
    meshok.remove(bochonok[0])  # исключаем выбранные цифры из списка чтобы не попадались вновь
    return bochonok

def action():
    number = bochonok()
    print('Доставли бочёнок с номером: ', number)
    print(gamer)
    print(pc)
    pc.card_update(number[0])
    while True:
        finalGamer = gamer.final()
        finalPC = pc.final()
        if finalGamer != 0:
            pass
        elif finalPC != 0:
            print("!!!You are LOOSER!!!")
            break
        else:
            print("!!!You are WINNER!!!")
            break
        choice = input('Есть такое число на карточке? (1 = Да, 2 = Нет) ')
        check = gamer.checking_number(number[0])
        if choice in ['1', '2']:
            if choice == '1' and check == 'Yes':
                gamer.card_update(number[0])
                action()
            elif choice == '2' and check == 'No':
                action()
            else:
                print('-=GAME OVER=-')
                exit(0)
        else:
            print('Можно выбрать только 1 = Да или 2 = Нет')
            continue

meshok = [x for x in range(1, 90)]  # генерируем список всех чисел
gamer = LotoCard('GAMER')
pc = LotoCard('PC')

action()