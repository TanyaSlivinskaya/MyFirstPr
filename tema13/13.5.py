"""Паттерн «Стратегия»
• Создайте класс Calculator, который использует разные стратегии для выполнения математических операций.
• Создайте несколько классов, каждый реализует определенную стратегию математической операции, например, Addition,
Subtraction, Multiplication, Division. Каждый класс должен содержать метод execute, который принимает два числа и
выполняет соответствующую операцию.
• Calculator должен иметь метод set_strategy, который устанавливает текущую стратегию, и метод calculate, который
выполняет операцию с помощью текущей стратегии"""

class Calculator:
    def init(self, strategy=None):
        self._strategy = strategy

    def Strategy(self, strategy):
        self._strategy = strategy

    def Calculate(self, a, b):
        return self._strategy.execute(a, b)

class Addition():
    def execute(self, a, b):
        return a+b

class Subtraction():
    def execute(self, a, b):
        return a - b

class Multiplication():
    def execute(self, a, b):
        return a * b

class Division():
    def execute(self, a, b):
        return a / b

calc = Calculator()

calc.Strategy(Addition())

print("Addition:", calc.Calculate(10, 69))