class Washing:
    def __init__(self, water):
        self.water = water

    def wash(self, item):
        print(f"I'm washing {item} with {self.water} l of water")


class Driving:
    def drive(self, a, b):
        print(f"Я везу из {a} в {b}")


class Machine:
    def __init__(self, brand, price, year, color):
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color


class Driving_Machine(Machine, Driving):
    pass


class Washing_Machine(Washing, Machine):
    def __init__(self, water, brand, price, year, color):
        super(Washing_Machine, self).__init__(water)
        self.brand = brand
        self.price = price
        self.year = year
        self.color = color


a1 = Driving_Machine('a', 10, '2020', 'red')
print(a1.color, a1.brand)
a1.drive(5, 6)
a2 = Washing_Machine(10, 'a', 5, '202', 'green')
print(a2.price)
a2.wash('showel')
a3 = Driving_Machine('b', 20, '240', 'yellow')
print(a3.price, a3.year)
