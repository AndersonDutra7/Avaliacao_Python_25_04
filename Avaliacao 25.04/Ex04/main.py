from carro import Carro

car1 = Carro(0,0,0)
car2 = Carro(0,0,0)
car3 = Carro('Renault', 'Duster', 2018)

car1.marca = input('Digite a marca do veículo: ')
car1.modelo = input('Digite o modelo do veículo: ')
car1.ano = input('Digite o ano do veículo: ')

car2.marca = input('Digite a marca do veículo: ')
car2.modelo = input('Digite o modelo do veículo: ')
car2.ano = input('Digite o ano do veículo: ')


car1.mostrar_informacoes()
car2.mostrar_informacoes()
car3.mostrar_informacoes()
