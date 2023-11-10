p = float(input('PESO:(KG) '))
a = float(input('ALTURA:(M) '))

imc = p / a**2

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBRE PESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
