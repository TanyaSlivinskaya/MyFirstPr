"""Дан список чисел. С помощью map() получить список,
где каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]"""


a = [1, 2, 3]

print(list(map(lambda x: str(x), a)))