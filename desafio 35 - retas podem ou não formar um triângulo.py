a = int(input('reta 1: '))
b = int(input('reta 2: '))
c = int(input('reta 3: '))

if  a < b + c and c < a + b  and b < c + a:
    print('Pode existir triângulo')
else:
    print('Não pode existir triângulo')
