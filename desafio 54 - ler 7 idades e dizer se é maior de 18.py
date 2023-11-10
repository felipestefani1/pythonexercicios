from datetime import datetime
year = datetime.today().year
ma = 0
me = 0
for c in range(1, 8):
    n = int(input('Ano nascimento: '))
    if year - n >= 18:
        ma = ma + 1
    else:
        me = me + 1
print('{} pessoas atingiram a maioridade!'.format(ma))
print('{} ainda não atingiram a maioridade!'.format(me))
