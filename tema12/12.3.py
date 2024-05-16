"""3. Класс «Автобус».
Класс содержит свойства:
● Скорость
● Максимальное количество посадочных мест
● Максимальная скорость
● Список фамилий пассажиров
● Флаг наличия свободных мест
● Словарь мест в автобусе
Методы:
● Посадка и высадка одного или нескольких пассажиров
● Увеличение и уменьшение скорости на заданное значение
● Операции in, += и -= (посадка и высадка пассажира по
фамилии)"""
class Bus:
    def __init__(self, speed, max_seats, max_speed):
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []
        self.available_seats = max_seats
        self.seats = {i: None for i in range(1, max_seats + 1)}

    def board(self, *passengers):
        for passenger in passengers:
            if self.available_seats > 0:
                for seat, value in self.seats.items():
                    if not value:
                        self.passengers.append(passenger)
                        self.seats[seat] = passenger
                        self.available_seats -= 1
                        break
            else:
                print("No available seats")

    def disembark(self, *passengers):
        for passenger in passengers:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                for seat, value in self.seats.items():
                    if value == passenger:
                        self.seats[seat] = None
                        self.available_seats += 1
                        break

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            print("Exceeded maximum speed")

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            print("Speed cannot be negative")

    def __contains__(self, passenger):
        return passenger in self.passengers

    def __iadd__(self, passenger):
        self.board(passenger)
        return self

    def __isub__(self, passenger):
        self.disembark(passenger)
        return self