i = int(input('Idade: '))

if i <= 9:
    print('MIRIM')
elif 9 < i <= 14:
    print('INFANTIL')
elif 14 < i <= 19:
    print('JUVENIL')
elif 19 < i <= 20:
    print('SENIOR')
else:
    print('MASTER')
