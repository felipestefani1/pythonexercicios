#for c in range (1,10):
#    print(c)
#print('Fim')

#c = 1
#while c < 10:
#    print(c)
#    c += 1
#print('Fim')

#n = 1
#while n != 0:
#    n = int(input('Número: '))
#print('Fim')


#r = 'S'
#while r == 'S':
#    n = int(input('Número: '))
#    r = str(input('Continuar?[S/N]'))
#print('Fim')

n = 1
par = 0
ímpar = 0
while n != 0:
    n = int(input('Número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            ímpar += 1
print('Números pares: {}'.format(par))
print('Números ímpares: {}'.format(ímpar))
