"""Реализовать функцию, которая создаёт матрицу размером
M строк на N столбцов и заполняет её рандомными числами"""

from random import randint
a = []
m = int(input())
n = int(input())


def matrix():
    for i in range(m):
        b = []
        for j in range(n):
            b.append(randint(10, 20))
        a.append(b)
    for b in a:
        for num in b:
            print(num, end=" ")
        print()

matrix()
