num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digíte um valor: ')))
    resp = str(input('Quer continar? [S/N]')).upper()
    if 'N' in resp:
        break

for i, v in enumerate(num):zz
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)

print('-='*30)
num.sort()
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
