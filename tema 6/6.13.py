"""Реализовать функцию, которая находит сумму элементов
на главной диагонали и сумму элементов на побочной диагонали
(матрица M x N)"""
a = [
    [17, 13, 11, 17, 10],
    [14, 14, 20, 12, 17],
    [18, 17, 19, 18, 18],
    [16, 18, 17, 15, 15],
    [13, 15, 19, 15, 19]
]

def summa():
    c = 0
    d = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j:
                c += a[i][j]
            # print(c)

    for i in range(len(a)):
        for j in range(len(a[i])):
            if i + j == len(a[i]) - 1:
                d += a[i][j]
            # print(d)
    print(c, d)

summa()

