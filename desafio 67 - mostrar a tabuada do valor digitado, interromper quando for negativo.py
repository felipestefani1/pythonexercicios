n = 0
while True:
    print('-'*40)
    n = int(input('Você quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
