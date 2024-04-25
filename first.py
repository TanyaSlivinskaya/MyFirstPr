"""Используя map() и reduce() посчитать площадь квартиры,
имея на входе характеристики комнат квартиры. Пример входных
данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},]"""
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]
from functools import reduce

x = reduce(lambda z,y: z + y,(list(map(lambda x: x['length']*x['width'], rooms ))))

print(x)

