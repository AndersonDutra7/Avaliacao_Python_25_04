# 7-Crie uma classe chamada Restaurante, esta classe deve conter dois atributos:um nome e um tipo_cozinha.
# Crie um método chamado descreve_restauranet() que imprima essas duas informações,
#  um método chamado abrir_restaurante() que imprima uma mensagem indicando que o restaurante está aberto
#  e um método chamado fechar_restaurante() que imprima uma mensagem indicando que o restaurante está fechado.
# Faça uma instância da classe Restaurante de sua classe.
# Imprima os dois atributos individualmente e depois invoque ambos os métodos.

from restaurante import  Restaurante

rest1 = Restaurante("Restaurante Brasa Viva", "Churrascaria")

print(rest1.nome)
print(rest1.tipo_cozinha)

rest1.descreve_restaurante()
rest1.abrir_restaurante()
rest1.fechar_restaurante()