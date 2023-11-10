p = float(input('PREÇO DO PRODUTO: '))
pag = str(input('Para pagar em dinheiro dinheiro a vista digite [1], '
              'para pagar a vista no cartão digite [2],'
              ' para pagar em até 2x no cartão digite [3] '
              'e para pagar em 3x ou mais no cartão digite [4]!'))

din = p - (p * 10/100)
car = p - (p * 5/100)
car2 = p
car3 = p + (p * 20/100)

if pag == '1':
    print('O valor será de R${}!'.format(din))
elif pag == '2':
    print('O valor será de R${}!'.format(car))
elif pag == '3':
    print('O valor será de R${}!'.format(car2))
elif pag == '4':
    print('O valor será de R${}'.format(car3))
