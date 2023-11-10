import random
from time import sleep

words = ('PEDRA', 'PAPEL', 'TESOURA')
word = random.choice(words)

print('VAMOS JOGAR JOKENPÔ')
print('-'*19)
e = str(input('Digite a sua escolha e digite, PEDRA, PAPEL OU TESOURA!'))
e = e.upper()

print('VOCÊ JOGOU {}'.format(e))
print('A MAQUINA JOGOU {}'.format(word))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-'*30)

if e == 'TESOURA' and word  == 'PEDRA':
    print('Você Perdeu :(')
elif e == 'TESOURA' and word == 'PAPEL':
    print('Você Ganhou :)')
elif e == 'PAPEL' and word == 'PEDRA':
    print('Você Ganhou :)')
elif e == 'PAPEL' and word == 'TESOURA':
    print('Você Perdeu :(')
elif e == 'PEDRA' and word == 'TESOURA':
    print('Você Ganhou :)')
elif e == 'PEDRA' and word == 'PAPEL':
    print('Você Perdeu :(')
else:
    print('O JOGO EMPATOU!')
