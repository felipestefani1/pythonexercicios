listanum = []
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        ('Valor duplicado! Não vou aceitar...')


    continuar = str(input('Você quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print('-='*40)
print(listanum)