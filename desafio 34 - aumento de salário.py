s = int(input('Digite o seu salário: '))
if s > 1250:
    print('Seu novo salário é {}'.format(s * 10/100 + s))
else:
    print('seu novo salário é {}'.format(s * 15/100 + s))

