from retangulo import Retangulo

r1 = Retangulo(0,0)

print('\033[1;32m#' * 24)
print('calculador de retângulos'.upper())
print('#' * 24 + '\033[0m')

r1.base = input('Digite a base: ')
r1.altura = input('Digite a altura: ')

print(f'A área do retãngulo é {r1.calcular_area(r1.base, r1.altura)}.')

