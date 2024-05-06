class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b

        print("Сложение:", result)

    def subtraction(self):
        result = self.a - self.b

        print("Вычитание:", result)

    def multiplication(self):
        result = self.a * self.b

        print("Произведение:", result)

    def division(self):
        result = self.a / self.b

        print("Деление", result)

math_operations1 = Math(6,7)
math_operations1.addition()

math_operations2 = Math(3,7)
math_operations2.subtraction()

math_operations3 = Math(8,7)
math_operations3.multiplication()

math_operations4 = Math(89,7)
math_operations4.division()
