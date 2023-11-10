lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')

for c in lanche:
    print(f'Eu vou comer {c}')
print('-'*40)

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('Eu comi pra caramba!')
print('-'*40)
#OU

for cont in range (0, len(lanche)):
    print(f'Eu  vou comer {lanche[cont]} na posição {cont}')
print('-'*40)

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
x = a + b
y = b + a
print(x)
print(y)
print(x.index(4))
del(y)
