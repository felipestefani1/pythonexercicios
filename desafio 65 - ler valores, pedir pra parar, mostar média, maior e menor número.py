cont = n = maior = menor = soma = 0
parar = ''

while parar != 'S':
    n = int(input('Digite mais um valor: '))
    parar = str(input('Deseja parar? [S/N]')).strip().upper()[0]
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
média = soma / cont

print('A média entre os {} números escritos é {:.2f}'.format(cont, média))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
