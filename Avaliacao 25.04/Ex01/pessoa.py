# 1-Observando o diagrama abaixo crie uma classe pessoa,
# a instancie, adicionando seus atributos e mostre os valores dos atributos da instância criada
# e crie a função caminhar da classe Pessoa,atente-se aos parâmetros e retorno da função.
# O retorno deve ser uma string que diga que a pessoa está caminhando x passos,onde x é a quantidade de passos que foi recebida por parâmetro.

class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade


    def caminhar(self, passos):
        if type(passos) == int:
            return print(f'{self.nome} esta caminhando {passos} passos.')
        else:
            print('Por favor, digite um número inteiro"')

