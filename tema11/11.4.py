"""Программа с классом Sphere для представления сферы в трёхмерном пространстве.
Реализовать методы:
o Конструктор, принимающий 4 числа: радиус и координаты центра сферы x, y, z. Если конструктор вызывается без аргументов, создать объект сферы с единичным радиусом и центром в начале координат.
Если конструктор вызывается только с радиусом, создать объект с соответствующим радиусом и центром в начале координат
o Метод get_volume(), возвращающий число – объем шара,ограниченного текущей сферой
o Метод get_square(), возвращающий число – площадь внешней поверхности сферы
Метод get_radius(), возвращающий число – радиус текущей сферы
o Метод get_center(), возвращающий кортеж с координатами центра сферы
o Метод set_radius(radius), который принимает новое значение радиуса, меняет радиус текущей сферы и ничего не возвращает
o Метод set_center(x, y, z), который принимает новые значения для координат центра радиуса, меняет координаты текущей сферы и ничего не возвращает
o Метод is_point_inside(x, y, z), который принимает координаты некой точки в трёхмерном пространстве и возвращает True или False в зависимости от того, находится ли точка внутри сферы"""

import math
class Sphere:
    def __init__(self, x = 0, y = 0, z = 0, r = 1 ):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
    def get_volume(self):
        return 4/3 * math.pi * pow(self.r, 3)

    def get_square(self):
        return 4 * math.pi * pow(self.r, 2)

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r = 1):
        self.r = r
        return self.r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2 < self.r:
            return True
        else:
            return False



s = Sphere()
print(s.set_radius())
s.set_radius(5)
print(s.set_radius())
print(s.get_volume())

