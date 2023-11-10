tothomens = maiorque18 = mulheres20 = 0
while True:
    print('-'*40)
    print('CADASTRE UMA PESSOA')
    print('-'*40)
    idade = int(input('Idade: '))
    if idade > 18:
        maiorque18 += 1
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo == 'M':
        tothomens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('-'*40)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print('='*7, 'FIM DO PROGRAMA', '='*7)
print(f'Total de pessoas com mais de 18 anos: {maiorque18}')
print(f'Ao todo temos {tothomens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
