# class ExQuote:
#     def __init__(self, quote):
#         self.quote = quote
#
#     def say(self):
#         return self.quote + '!'
#
#
# class QQuote:
#     def __init__(self, quote):
#         self.quote = quote
#
#     def say(self):
#         return self.quote + '!'
#
# a = ExQuote('...')
# b = QQuote('///')
# print(a.say())
# print(b.say())

class Counter:  #getter
    # __current = 0

    def __init__(self):
        self.__current = 0

    def __add(self):
        self.__current += 1

    def add(self):
        self.__current += 1

    def to_zero(self):
        self.__current = 0

    def get_current(self):
        return self.__current

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def say(self):
        print(f'Привет, я Человек. Меня зовут {self.name}, мой возраст - {self.age}, я проживаю в стране под названием {self.country}')

class Student(Person):
    def __init__(self, age, name, country, study, __num_parrent):
        self.age = age
        self.name = name
        self.country = country
        self.study = study
        self.__num_parrent = __num_parrent

    def set_num(self, num):
        self.__num_parrent = num


    def get_number(self):
        return self.__num_parrent

    # def __eq(self, other): "=="
    #     return (self.name == other.name) and (self.age == other.age)
    # __ne__ "!=" not eqaul
    # __lt__ "<" lower then
    # __qt__ ">" greater then
    # __le__ "<=" lower equal
    # __ge__ ">=" greater equal
    # __add__
    # __sub__
    # __mul__
    # __pow__
    # __mod__

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __gt__(self, other):
        return(self.x > other.x) and (self.y > other.y)

    def __le__(self, other):
        if self.x == other.x:
            return self.y < other.y
        elif self.y == other.y:
            return self.y < other.y
        else:
            return False

    def __ge__(self, other):
        if self.x == other.x:
            return self.y > other.y
        elif self.y == other.y:
            return self.y > other.y
        else:
            return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return  Dot(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return  Dot(x, y)

c = Counter()
c._Counter__add()
c.add()
print(c._Counter__current)
c.to_zero()
print(c.get_current())
b = Student(15, 'Ggf', 'LLL', '12', 88005553535)
print(b._Student__num_parrent)
b.set_num(89999999999)
print(b.get_number())