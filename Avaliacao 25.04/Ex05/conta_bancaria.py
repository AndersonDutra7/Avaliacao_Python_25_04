# 5-Crie uma classe Conta Bancaria que tenha os atributos titular e saldo.
# Crie métodos na classe para depositar e sacar dinheiro da conta.
# Crie um objeto dessa classe,faça um depósito e um saque, e imprima o saldo final.

class Conta_Bancária:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor

