n = int(input('Quantos termos mostrar: '))
cont = 3
fb1 = 0
fb2 = 1
fbn = 0

print('{} -> {} -> '.format(fb1, fb2), end='')
while cont <= n:
    fbn = fb1 + fb2
    fb1 = fb2
    fb2 = fbn
    print('{} -> '.format(fbn), end='')
    cont += 1
print('Fim')

