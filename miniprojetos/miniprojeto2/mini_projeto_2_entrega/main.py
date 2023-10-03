from miniprojetos.miniprojeto2.mini_projeto_2_entrega.codigo_geometrico.circulo import Circulo
from miniprojetos.miniprojeto2.mini_projeto_2_entrega.codigo_geometrico.retangulo import Retangulo
from miniprojetos.miniprojeto2.mini_projeto_2_entrega.codigo_geometrico.triangulo import Triangulo

def main():
    print("Bem-vindo ao código geométrico!")

    escolha = 0
    retangulo_num = 1
    triangulo_num = 1
    circulo_num = 1
    retangulos = []
    triangulos = []
    circulos = []

    while escolha != 6:
        print("\nEscolha uma ação:")
        print("1. Definir um retângulo")
        print("2. Definir um triângulo")
        print("3. Definir um círculo")
        print("4. Listar as formas armazenadas")
        print("5. Ordenar tamanhos de área")
        print("6. Sair\n")

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
        elif escolha != 6:
            print("\nObrigado por usar o código geométrico!")

if __name__ == "__main__":
    main()
