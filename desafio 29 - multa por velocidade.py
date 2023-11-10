v = int(input('Velocidade: '))
m = 0
va = v - 80
if v > 80:
    print('Você passou a {}KM/H, fora da velocidade permitida!'.format(v))
    print('Você deverá pagar de multa R${}'.format(va*7))



