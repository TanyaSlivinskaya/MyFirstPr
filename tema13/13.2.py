"""Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся пользователем с
клавиатуры."""

def infinite_sequence(seq):
    while True:
        for item in seq:
            yield item

def main():
    sequence = [1, 2, 3]
    n = int(input("введите количество чисел последовательности,которые вы хотите увидеть"))

    generator = infinite_sequence(sequence)

    for a in range(n):
        print(next(generator))

main()