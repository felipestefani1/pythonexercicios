números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        print('Valor duplicado! Não vou aceitar...')
    r = str(input('Você quer continuar? [S/N]')).strip().upper()
    if r in 'Nn':
        break
print('-='*40)
números.sort()
print(números)