from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0

while opção != 5:
    print('''    [1]Somar 
    [2]Multiplicar 
    [3]Maior 
    [4]Novos números 
    [5]Sair do programa''')
    opção = int(input('O que você deseja fazer? '))
    if opção == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1+n2))
    elif opção == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é o: {}'.format(n1, n2, n1))
        else:
            print('O maior número entre {} e {} é o {}'.format(n1, n2, n2))
    elif opção == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(1)
print('Fim!')
