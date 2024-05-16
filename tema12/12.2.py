"""Экземпляр класса инициализируется двумя целыми числами, первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● Fly() – возвращает True, если часть пчелы не меньше части слона, иначе – False
● Trumpet() – если часть слона не меньше части пчелы, возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● Eat(meal, value) – может принимать в meal только ”nectar” или “grass”. Если съедает нектар, то value вычитается из части
слона, пчеле добавляется. Иначе – наоборот. Не может увеличиваться больше 100 и уменьшаться меньше 0."""
class ЕlephantAndBee:

    def init(self, elefant, bee):
        self.elefant = elefant
        self.bee = bee

    def fly(self):
        return self.bee > self.elefant

    def trumpet(self):
        if self.elefant >= self.bee:
            return f"tu-tu-doo-doo"
        else:
            return f"wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elefant -= value
            self.bee += value

        else:
            self.elefant += value
            self.bee -= value

        if self.elefant > 100:
            return self.elefant == 100
        elif self.elefant < 0:
            return self.elefant == 0
        if self.bee > 100:
            return self.bee == 100
        elif self.bee < 0:
            return self.bee == 0





a = ЕlephantAndBee(9, 12)
print(a.trumpet())


print(a.eat(56,98), )

