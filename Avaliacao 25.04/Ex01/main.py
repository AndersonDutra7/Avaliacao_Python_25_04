from pessoa import Pessoa

p1 = Pessoa(1, 'Anderson', 36)
p2 = Pessoa(2, 'Thalya', 33)
p3 = Pessoa(3, 'Letícia', 2)

print(f'{p1.nome} esta estudando.')
print(f'O id de {p2.nome} é {p2.id}.')
print(f'{p3.nome} possui {p3.idade} anos.')

p1.caminhar('50')
p2.caminhar(40)
p3.caminhar(15)



