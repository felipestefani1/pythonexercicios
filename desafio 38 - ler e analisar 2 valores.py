a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a > b:
    print('{} é maior que {}'.format(a,b))
elif b > a:
    print('{} é maior que {}'.format(b,a))
else:
    print('{} é igual a {}'.format(a,b))
