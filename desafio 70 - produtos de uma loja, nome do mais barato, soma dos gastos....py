somavalores = maisquemil = soma = menorvalor = nomemenor = 0

print('-'*40)
print('LOJA SUPER BARATÃO')
print('-'*40)

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    somavalores += preço
    if preço > 1000:
        maisquemil += 1
    soma += 1
    if soma == 1:
        menorvalor = preço
        nomemenor = nome
    if preço < menorvalor:
        menorvalor = preço
        nomemenor = nome
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('========= FIM DO PROGRAMA =========')
print(f'O total da compre foi de R${somavalores}')
print(f'Temos {maisquemil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomemenor} que custa R${menorvalor}')
