# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод

import time
from itertools import cycle


class TrafficLight:
    _color = ['red', 'yellow', 'green']

    def runnig(self):
        for color in cycle(TrafficLight._color):
            if color == 'red':
                print(color)
                time.sleep(7)
            elif color == 'yellow':
                print(color)
                time.sleep(2)
            elif color == 'green':
                print(color)
                time.sleep(4)


mode = TrafficLight()
mode.runnig()

# color = ['red', 'yellow', 'green']
# iter = cycle(color)
#
# print(next(iter))
# print(next(iter))
