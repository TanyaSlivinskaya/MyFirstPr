"""Программа получает на вход два числа и находит их НОД
(наибольший общий делитель). Пример: на вход подаются числа 12
и 18, их НОД равен 6."""

from math import gcd
a = int(input("Введите число 1"))
b = int(input("Введите число 2"))

def fun():
    print(gcd(a, b))


fun()