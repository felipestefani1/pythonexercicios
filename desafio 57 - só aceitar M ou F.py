#s = ' '
#while s not in 'FM':
#    s = str(input('Digite seu sexo:[M/F]: ')).strip()
#    if s not in 'FM':
#        print('Sexo inválido, tente novamente')
#    else:
#        print('Sexo válido!')
#print('Fim')

# DUAS FORMAS DE FAZER

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por Favor, informe seu sexo: [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


