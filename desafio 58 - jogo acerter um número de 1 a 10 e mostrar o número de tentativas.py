from random import randrange
númeropc = randrange(0, 10)
númerojogador = 11
númerotentativas = 0
while númeropc != númerojogador:
    númerojogador = int(input('Digite um número entre 0 e 10: '))
    númerotentativas += 1

print('O número que o computador pensou foi {}'.format(númeropc))
print('Você teve de usar {} tentativas para acertar!'.format(númerotentativas))
print('Fim!')
