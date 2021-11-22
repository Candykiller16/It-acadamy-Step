# Задание 1
# Создайте базовый класс Equation с методом solve (вычислить корни уравнения).
# Создайте производные классы для линейных уравнений LinearEquation и для квадратных уравнений QuadraticEquation. \
# Реализуйте в каждом из них метод solve.

import math
class Equation:
    def __init__(self, a='', b='', c =''):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        pass

class LinearEquation(Equation):
    def solve(self):
        print("Введите коэффициенты для уравнения")
        self.a = float(input('a = '))
        self.b = float(input('b = '))
        if self.a == 0 and self.b == 0:
            print('Бесконечное количество решений')
        elif self.a == 0 and self.b != 0:
            print('Нет корней')
        else:
            print(-self.b/self.a)


class QuadraticEquation(Equation):
    def solve(self):
        print("Введите коэффициенты для уравнения")
        print("ax^2 + bx + c = 0:")
        self.a = float(input("a = "))
        self.b = float(input("b = "))
        self.c = float(input("c = "))

        discr = self.b ** 2 - 4 * self.a * self.c
        print('Дискриминант = {}'.format(discr))

        if discr > 0:
            x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
            print('x1 = {0}, x2 = {1}'.format(x1, x2))
        elif discr == 0:
            x = -self.b / (2 * self.a)
            print('x = {}'.format(x))
        else:
            print("Корней нет")

# linear = LinearEquation()
# linear.solve()

# quadratic = QuadraticEquation()
# quadratic.solve()


class Pet:
    def __init__(self, breed = '', name = '', age=10, sound = '', type = ''):
        self._breed = breed
        self._name = name
        self._age = age
        self._sound = sound
        self._type = type

    def show(self):
        print(self._name)

    def sound(self):
        print(self._sound)

    def type(self):
        print(f"It's a {self._type}")

class Dog(Pet):
    def __init__(self, breed, name, age, sound, type, hight):
        super(Dog, self).__init__(breed, name, age, sound, type)
        self._hight = hight

    def description(self):
        print(f'{self._breed} {self._type} {self._name} is {self._age} years old')

class Cat(Pet):
    def __init__(self, breed, name, age, sound, type, hight):
        super(Cat, self).__init__(breed, name, age, sound, type)
        self._hight = hight

    def description(self):
        print(f'{self._breed} {self._type} {self._name} is {self._age} years old')

Tom = Cat(breed='Siam', name='Tom', age=10, sound='МЯУ', type='Cat', hight='100см')
# Tom.sound()
# Tom.show()
# Tom.type()
# Tom.description()


Buch = Dog(breed='Buldog', name='Buch', age=12, sound='ГАУ', type='Dog', hight='150см')
# Buch.sound()
# Buch.show()
# Buch.type()
# Buch.description()