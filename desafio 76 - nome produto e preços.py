listagem = ('Pão', 2.50, 'Borracha', 3.99, 'Trident', 5.09, 'Refrigerante', 7.90, 'Livro', 35.90)

print(f'{"LISTAGEM DE PREÇOS":^40}')

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')