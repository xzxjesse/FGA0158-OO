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

    while escolha != 7:
        print("\nEscolha uma ação:")
        print("1. Definir um retângulo")
        print("2. Definir um triângulo")
        print("3. Definir um círculo")
        print("4. Listar as formas armazenadas")
        print("5. Ordenar tamanhos de área")
        print("6. Editar uma forma")
        print("7. Sair\n")

        escolha = int(input("Digite o número da ação desejada: "))

        if escolha == 1:
            retangulo = Retangulo(retangulo_num)
            retangulo.definir(f"retângulo {retangulo_num}")
            retangulo.calcular_area()
            retangulos.append(retangulo)
            print(f"A área do retângulo {retangulo.num} é: {retangulo.area:.2f}\n")
            retangulo_num += 1
        elif escolha == 2:
            triangulo = Triangulo(triangulo_num)
            triangulo.definir(f"triângulo {triangulo_num}")
            triangulo.calcular_area()
            triangulos.append(triangulo)
            print(f"A área do triângulo {triangulo.num} é: {triangulo.area:.2f}\n")
            triangulo_num += 1
        elif escolha == 3:
            circulo = Circulo(circulo_num)
            circulo.definir_raio()
            circulo.calcular_area()
            circulos.append(circulo)
            print(f"A área do círculo {circulo.num} é: {circulo.area:.2f}\n")
            circulo_num += 1
        elif escolha == 4:
            formas = retangulos + triangulos + circulos
            if not formas:
                print("Não há nenhuma forma geométrica armazenada.\n")
            else:
                print("As formas geométricas armazenadas são:\n")
                for i, forma in enumerate(formas, start=1):
                    print(f"{forma.__class__.__name__} {forma.num} - Área: {forma.area:.2f}")
        elif escolha == 5:
            formas = retangulos + triangulos + circulos
            if not formas:
                print("Não há nenhuma forma geométrica armazenada.\n")
            else:
                print("A ordem de tamanho da área das formas armazenadas é:\n")
                formas.sort(key=lambda forma: forma.area, reverse=True)
                for i, forma in enumerate(formas, start=1):
                    print(f"{forma.__class__.__name__} {forma.num} - Área: {forma.area:.2f}")
        elif escolha == 6:
            formas = retangulos + triangulos + circulos
            print("\nEscolha a forma que deseja editar:")

            for i, forma in enumerate(formas, start=1):
                print(f"{i}. {forma.__class__.__name__} {forma.num}")

            escolha_forma = int(input("Digite o número da forma que deseja editar: "))
    
            if 1 <= escolha_forma <= len(formas):
                forma = formas[escolha_forma - 1]
                if isinstance(forma, Retangulo) or isinstance(forma, Triangulo):
                    forma.definir(f"{forma.__class__.__name__} {forma.num}")
                    forma.calcular_area()
                elif isinstance(forma, Circulo):
                    forma.definir_raio()
                    forma.calcular_area()
                print(f"A área da forma {forma.__class__.__name__} {forma.num} foi atualizada para: {forma.area:.2f}\n")
            else:
                print("Opção inválida!")        
            
        elif escolha != 7:
            print("\nObrigado por usar o código geométrico!")

if __name__ == "__main__":
    main()