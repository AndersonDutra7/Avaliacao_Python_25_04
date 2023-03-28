import datetime

class Restaurante:

    nome = ""
    tipo_cozinha = ""

    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha

    def descreve_restaurante(self):
        print(f"Restaurante: {self.nome} - Tipo: {self.tipo_cozinha}.")

    def abrir_restaurante(self):
        hora_atual = int(datetime.datetime.now().hour)
        if hora_atual > 10 and hora_atual <= 15 :
            print(f"Seja Bem Vindo! O {self.nome} esta aberto até as 15 horas.")

    def fechar_restaurante(self):
        hora_atual = int(datetime.datetime.now().hour)
        if (hora_atual < 10) or (hora_atual > 15):
            print(f"Olá Amigo! O horário de funcionamento {self.nome} é das 10:00 até as 15:00 horas.")
