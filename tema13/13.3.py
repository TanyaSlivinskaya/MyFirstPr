"""3. Паттерн «Строитель»
● Создайте класс Pizza, который содержит следующие атрибуты: size, cheese, pepperoni, mushrooms, onions,
bacon.
● Создайте класс PizzaBuilder, который использует паттерн «Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из атрибутов Pizza.
● Создайте класс PizzaDirector, который принимает экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza."""
class Pizza():
    def init(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

class PizzaBuilder():

    def init(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False


    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)


class PizzaDirector:
    def init(self, builder):
        self.builder = builder

    def make_pizza(self):
        self.builder.add_cheese().add_pepperoni().add_mushrooms().add_onions().add_bacon()
        return self.builder.build()

builder = PizzaBuilder("big")
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)