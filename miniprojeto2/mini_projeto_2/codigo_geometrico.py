import math

class BaseAltura:
    def __init__(self):
        self.base = 0.0
        self.altura = 0.0

    def definir(self):
        self.base = float(input("Digite a base: "))
        self.altura = float(input("Digite a altura: "))

class Retangulo(BaseAltura):
    def __init__(self):
        super().__init__()
        self.area = 0.0

    def calcular_area(self):
        self.area = self.base * self.altura

class Triangulo(BaseAltura):
    def __init__(self):
        super().__init__()
        self.area = 0.0

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

class Circulo:
    def __init__(self):
        self.raio = 0.0
        self.area = 0.0

    def definir_raio(self):
        self.raio = float(input("Digite o raio do círculo: "))

    def calcular_area(self):
        pi = 3.14159265359
        self.area = pi * self.raio ** 2

def main():
    print("Bem-vindo ao pseudocódigo geométrico!")

    escolha = 0
    while escolha != 5:
        print("Escolha uma forma geométrica:")
        print("1. Retângulo")
        print("2. Triângulo")
        print("3. Círculo")
        print("4. Ordenar tamanhos de área")
        print("5. Sair")

        escolha = int(input("Digite o número da forma desejada: "))

        if escolha == 1:
            retangulo = Retangulo()
            retangulo.definir()
            retangulo.calcular_area()
            print("A área do retângulo é:", retangulo.area)
        elif escolha == 2:
            triangulo = Triangulo()
            triangulo.definir()
            triangulo.calcular_area()
            print("A área do triângulo é:", triangulo.area)
        elif escolha == 3:
            circulo = Circulo()
            circulo.definir_raio()
            circulo.calcular_area()
            print("A área do círculo é:", circulo.area)
        elif escolha == 4:
            areas = [retangulo.area, triangulo.area, circulo.area]
            areas.sort(reverse=True)
            if areas[0] == retangulo.area:
                print("Retângulo > Triângulo > Círculo")
            elif areas[0] == triangulo.area:
                print("Triângulo > Retângulo > Círculo")
            else:
                print("Círculo > Retângulo > Triângulo")
        elif escolha != 5:
            print("Obrigado por usar o pseudocódigo geométrico!")

if __name__ == "__main__":
    main()
