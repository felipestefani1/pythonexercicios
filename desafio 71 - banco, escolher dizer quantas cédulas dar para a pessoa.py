ced50 = ced20 = ced10 = ced1 = 0

print('='*40)
print('BANCO CEV')
print('='*40)

sacar = int(input('Qual valor você quer sacar? '))

while sacar != 0:
    ced50 = sacar // 50
    sacar = sacar % 50

    ced20 = sacar // 20
    sacar = sacar % 20

    ced10 = sacar // 10
    sacar = sacar % 10

    ced1 = sacar // 1
    sacar = sacar % 1

print(f'Total de {ced50} cédular de R$50')
print(f'Total de {ced20} cédular de R$20')
print(f'Total de {ced10} cédular de R$10')
print(f'Total de {ced1} cédular de R$1')
