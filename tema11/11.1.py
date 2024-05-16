class Soda:
    def __init__(self, taste = None):
        self.taste = taste
    def __str__(self):
        return f"У вас газировка с {self.taste} вкусом" if self.taste else "У вас обычная газировка"

taste1 = Soda("малиновым")
print(taste1)
taste2 = Soda()
print(taste2)


