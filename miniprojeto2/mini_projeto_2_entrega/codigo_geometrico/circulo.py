from codigo_geometrico.base_altura import BaseAltura

class Circulo:
    def __init__(self, num):
        self.raio = 0.0
        self.area = 0.0
        self.num = num

    def definir_raio(self):
        self.raio = float(input(f"Digite o raio do círculo {self.num}: "))

    def calcular_area(self):
        pi = 3.14159265359
        self.area = round(pi * self.raio ** 2, 2)