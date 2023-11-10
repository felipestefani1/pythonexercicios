primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
ult = int(input('Quantos termos mostrar: '))
termo = primeiro
cont = 1

while cont <= ult:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim')
