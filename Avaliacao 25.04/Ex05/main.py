from conta_bancaria import Conta_Bancária

conta1 = Conta_Bancária('Anderson', 100)

while True:
    print('#'*50)
    print(f'BEM VINDO {conta1.titular}, qual operação queres realizar?'.upper())
    print('#'*50)
    print()

    opcao = input(f'\033[1;32mDigite ...\n"S"  >>> Saque\n"D" >>> Depósito\n\033[0m')
    opcao = opcao.upper()

    if opcao == "S":
        valor = input(f"Digite o valor para saque: ").replace(',', '.')
        if valor.isalnum():
            print('\033[1;31mValor digitado errado, refaça a operação!\033[0m\n')
        else:
            valor = float(valor)
            conta1.sacar(valor)
            print(f'Você sacou {valor:.2f}, logo seu saldo ficou em R${conta1.saldo:.2f}.')
            break
    elif opcao == "D":
        valor = input(f"Digite o valor a ser depositado: ").replace(',', '.')
        if valor.isalnum():
            print('\033[1;31mValor digitado errado, refaça a operação!\033[0m\n')
        else:
            valor = float(valor)
            conta1.depositar(valor)
            print(f'Você depositou {valor:.2f}, logo seu saldo ficou em R${conta1.saldo:.2f}.')
            break
    else:
        print('\033[1;31mOpção escolhida inválida, refaça a operação!\033[0m\n')