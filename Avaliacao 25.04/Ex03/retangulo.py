class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self, base, altura):
        base = int(base)
        altura = int(altura)
        return int(altura * base)