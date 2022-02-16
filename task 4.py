class Bakery:
    milk = 0.5

    def __init__(self, eggs=1, flour=2):
        self.eggs = eggs
        self.flour = flour

    def bake(self, temp, time):
        print(self.eggs, self.flour)
        print(temp, time)


class Cookie(Bakery):
    def __init__(self, eggs, flour, cinnamon):
        super(Cookie, self).__init__(eggs, flour)
        self.cinnamon = cinnamon

    def __del__(self):
        pass


class Car:
    steerling_wheel = True

    def __init__(self, color, engine, wheels):
        self.color = color
        self.engine = engine
        self.wheels = wheels

    def drive(self, speed, a, b, list_of_load):
        time = (a.place - b.place) / speed
        for item in list_of_load:
            item.place = b
        return time

class Ferrari(Car):
    def __init__(self, color, engine, wheels, ):
        if not (engine == 'v8' or engine == 'v12'):
            print('False')
            raise Exception
            return
        else:
            super(Ferrari, self).__init__(color, engine, wheels)
            self. manafact = 'Ferrari'

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def say(self):
        print(f'Привет, я Человек. Меня зовут {self.name}, мой возраст - {self.age}, я проживаю в стране под названием {self.country}')

class A:
    def shout(self):
        print('Whats your name')

    def say(self):
        print('I am obj A')

class B:
    def yell(self):
        print('Ezdlf')

    def say(self):
        print('I am obj B')

class C(A, B):
    pass

class Washing:

    def __init__(self, water, soap):
        self.water = water
        self.soap = soap

    def whas(self, item):
        self.item = item
        print(f'I wash {self.item}, i need {self.water} for it')

class Driving:
    def drive(self, a, b, speed):
        self.a = a
        self.b = b
        self.speed = speed
        print(f'I drive from {self.a} to {self.b} with speed - {self.spped}')

class Machine:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color



class Driving_Machine(Machine, Driving):
    pass

class Washing_Machine(Machine, Washing):
    pass

b = Bakery()
b.bake(180, 900)
car_1 = Car('red', 'v8', 6)
#car_1.drive(10, 8, 5, [5, 6, 7])
print(car_1.color)
car_2 = Ferrari('red', 'v8', 4)
print(car_2.manafact)
peop1 = Person('Josh', 19, 'Germany')
peop1.say()
c = C()
c.shout()
c.yell()
c.say()