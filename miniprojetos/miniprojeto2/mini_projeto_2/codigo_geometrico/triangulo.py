from codigo_geometrico.base_altura import BaseAltura
class Triangulo(BaseAltura):
    def __init__(self, num):
        super().__init__()
        self.area = 0.0
        self.num = num

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2