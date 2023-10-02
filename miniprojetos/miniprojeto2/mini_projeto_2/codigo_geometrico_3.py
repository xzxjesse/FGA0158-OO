import math

class BaseAltura:
    def __init__(self):
        self.base = 0.0
        self.altura = 0.0

    def definir(self, num):
        self.base = float(input(f"Digite a base do {num}: "))
        self.altura = float(input(f"Digite a altura do {num}: "))

class Retangulo(BaseAltura):
    def __init__(self, num):
        super().__init__()
        self.area = 0.0
        self.num = num

    def calcular_area(self):
        self.area = self.base * self.altura

class Triangulo(BaseAltura):
    def __init__(self, num):
        super().__init__()
        self.area = 0.0
        self.num = num

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

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

def main():
    print("Bem-vindo ao código geométrico!")

    escolha = 0
    retangulo_num = 1
    triangulo_num = 1
    circulo_num = 1
    retangulos = []
    triangulos = []
    circulos = []

    while escolha != 5:
        print("Escolha uma forma geométrica:")
        print("1. Retângulo")
        print("2. Triângulo")
        print("3. Círculo")
        print("4. Ordenar tamanhos de área")
        print("5. Sair")

        escolha = int(input("Digite o número da forma desejada: "))

        if escolha == 1:
            retangulo = Retangulo(retangulo_num)
            retangulo.definir(f"retângulo {retangulo_num}")
            retangulo.calcular_area()
            retangulos.append(retangulo)
            print(f"A área do retângulo {retangulo.num} é: {retangulo.area:.2f}")
            retangulo_num += 1
        elif escolha == 2:
            triangulo = Triangulo(triangulo_num)
            triangulo.definir(f"triângulo {triangulo_num}")
            triangulo.calcular_area()
            triangulos.append(triangulo)
            print(f"A área do triângulo {triangulo.num} é: {triangulo.area:.2f}")
            triangulo_num += 1
        elif escolha == 3:
            circulo = Circulo(circulo_num)
            circulo.definir_raio()
            circulo.calcular_area()
            circulos.append(circulo)
            print(f"A área do círculo {circulo.num} é: {circulo.area:.2f}")
            circulo_num += 1
        elif escolha == 4:
            formas = retangulos + triangulos + circulos
            formas.sort(key=lambda forma: forma.area, reverse=True)
            for i, forma in enumerate(formas, start=1):
                print(f"{forma.__class__.__name__} {forma.num} - Área: {forma.area:.2f}")
        elif escolha != 5:
            print("Obrigado por usar o código geométrico!")

if __name__ == "__main__":
    main()
