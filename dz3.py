# from random import randint

# 1)класс машины, скорость, имя
#     Car
# 2) класс гонки (закрытой нелегальной)
#     длина круга
#     play(list[Car], laps:int) ->list[Car]
#     на каждом круге происходит случ авария

import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Race:
    len_circle = 200

    def play(self, cars, circle):
        f = True
        finish = []
        while f:
            k = 0
            for i in range(len(cars) - 1):
                if cars[i].speed < cars[i + 1].speed:
                    cars[i], cars[i + 1] = cars[i + 1], cars[i]
                    k += 1
            if k == 0:
                f = False

        for _ in range(circle):
            lox = random.randint(0, len(cars)-1)
            car_lox = cars[lox]
            cars.remove(cars[lox])
            cars.append(car_lox)
        for i in cars:
            finish.append(i.name)
        return finish

a1 = Car('a1', 20)
print(a1.name)
a2 = Car('a2', 15)
print(a2.speed)
a3 = Car('a3', 40)
print(a3.name, a3.speed)
b = Race()
caras = [a1, a2, a3]
print(b.play(caras, 2))
