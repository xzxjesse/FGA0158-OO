class BaseAltura:
    def __init__(self):
        self.base = 0.0
        self.altura = 0.0

    def definir(self, num):
        self.base = float(input(f"Digite a base do {num}: "))
        self.altura = float(input(f"Digite a altura do {num}: "))