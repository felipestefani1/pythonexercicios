import random
from random import randrange

n = int(input('Digite um número entre 0 e 5: '))
np = randrange(0, 5)
print('Você escolheu {}'.format(n))
print('Nós escolhemos {}'.format(np))
if n == np:
    print('Você acertou o número!!!')
else:
    print('Você errou!!!')



