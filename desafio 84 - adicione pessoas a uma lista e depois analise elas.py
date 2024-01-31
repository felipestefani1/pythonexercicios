galera = list()
dado = list()
mai = men = 0
while True:
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite a sua idade: ')))
    if len(galera) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    continuar = str(input('Você quer continuar? [S/N]')).upper()

    if 'N' in continuar:
        break

print(f'Você cadastrou {len(galera)} pessoas')
print(f'A pessoa mais nova tem {men} anos')
print(f'A pessoa mais velha tem {mai} anos')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]} a mais velha')
for p in galera:
    if p[1] == men:
        print(f'{p[0]} a mais nova')
