
n = 0
soman = 0
cont = 0
while n != 999:
    n = int(input('Digite um valor: [999 para parar]'))
    soman += n
    cont += 1
print('A soma dos {} números digitados foi {}'.format(cont - 1, soman - 999))
print('Fim')
