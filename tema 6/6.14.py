"""Дана матрица M x N. Исходная матрица состоит из нулей и
единиц. Реализовать функцию, которая добавит к матрице ещё
один столбец, элементы которого делает количество единиц в
соответствующей строке чётным"""

a = [
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0]
]

def make_even(a):
    new_matrix = []
    for row in a:
        row.append(1 if row.count(1) % 2 != 0 else 0)
        new_matrix.append(row)
    return new_matrix

new_matrix = make_even(a)
for row in new_matrix:
    print(row)









