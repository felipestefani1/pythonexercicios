from random import randint

n = soma = v = 0
escolha = ''

print('=-'*40)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*40)

while True:
    númeropc = randint(0,10)
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar: [P/I]')).strip().upper()
    soma = n + númeropc
    print(f'Você jogou {n} e o computador jogou {númeropc}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU')
            v += 1
        else:
            print('VOCÊ PERDEU')
            print(f'GAMEOVER! Você venceu {v} vezes!')
            break
    if escolha == 'I':
        if soma % 2 != 0:
            print('VOCÊ VENCEU')
            v += 1
        else:
            print('VOCÊ PERDEU')
            print(f'GAMEOVER! Você venceu {v} vezes!')
            break




