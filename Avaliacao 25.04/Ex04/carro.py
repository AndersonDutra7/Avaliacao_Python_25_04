#4-Crie uma classe Carro que tenha os atributos marca, modelo e ano.
# Crie um método na classe para imprimir as informações do carro.
# Crie um objeto dessa classe e chame o método para imprimir suas informações.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_informacoes(self):
        print(f'Veículo Marca: {self.marca} - Modelo {self.modelo} - Ano: {self.ano}.')

