# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        # self.color = color
        self.model = name
        self.police = bool(is_police)
        print(f'Creatу new car - {self.model}')

    def go(self):
        print(f'{self.model} drive')

    def stop(self):
        print(f'{self.model} stop')

    def turn(self, direction):
        print(f'{self.model} turn {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Over speed!')
        else:
            print(f'Speed car: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Over speed!')
        else:
            print(f'Speed car: {self.speed}')


class PoliceCar(Car):
    pass


car1 = TownCar(70, 'Gray', 'Lada', False)
car1.go()
car1.turn('right')
car1.show_speed()
car1.stop()

car2 = WorkCar(45, 'Orange', 'ZIL', False)
car2.go()
car2.turn('left')
car2.turn('right')
car2.show_speed()
car2.stop()
