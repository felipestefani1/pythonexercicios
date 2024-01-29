valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('QUER CONTINUAR: [S/N]')).upper()
    if 'N' in resp:
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort()
print(f'Você digitou os valores {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')