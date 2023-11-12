palavras = ('bola', 'basquete', 'futebol', 'volei', 'gatorade',
            'churros', 'ambrosia', 'ameixa', 'batata')

for p in palavras:
    print(f'\nNa palavras {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')