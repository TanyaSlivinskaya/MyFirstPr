"""Программа получает на вход число H. Реализовать
функцию, которая определяет, какие столбцы имеют хотя бы одно
такое же число, а какие не имеют (матрица M x N)"""

a = [
    [17, 13, 11, 17, 10],
    [14, 14, 20, 12, 17],
    [18, 17, 19, 18, 18],
    [16, 18, 17, 15, 15],
    [13, 15, 19, 15, 19]
]
c = int(input())

def sovp():
    for j in range(len(a[0])):
        for i in range(len(a)):
            if a[i][j] == c:
                print("значение имеется в столбце", j + 1)
                break
        else:
            print("значение не имеется в столбце", j + 1)

sovp()






