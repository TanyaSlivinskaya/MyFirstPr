"""Программа с классом Car. При инициализации объекта ему
должны задаваться атрибуты color, type и year. Реализовать
пять методов. Запуск автомобиля – выводит строку
«Автомобиль заведён». Отключение автомобиля – выводит
строку «Автомобиль заглушен». Методы для присвоения
автомобилю года выпуска, типа и цвета"""


class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведён")
    def stop(self):
        print("Автомобиль заглушен")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year



