km = int(input('Distância da viagem em KM: '))
if km <= 200:
    print('O valor da viagem será de R${:.2f}'.format(km * 0.5))
else:
    print('O valor da viagem será de R${:.2f}'.format(km * 0.45))
