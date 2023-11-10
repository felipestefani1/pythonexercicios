
from datetime import datetime
year = datetime.today().year

nas = int(input('Em que ano você nasceu? '))
idade = year - nas    #idade
falt = 18 - idade    #quantos anos faltam para se alistar
pas = idade - 18    #a quantos anos se alistou

if idade < 18:
    print('Ainda faltam {} anos para você se alistar!'.format(falt))
elif idade == 18:
    print('Você deve se alistar!')
else:
    print('Você se alistou a {} anos!'.format(pas))

