a = int(input('RETA 1: '))
b = int(input('RETA 2: '))
c = int(input('RETA 3: '))

if a == b == c:
    print('Triângulo Equilátero!')
elif a < b + c and c < a + b  and b < c + a and a == b or b == c or a == c:
    print ('Triângulo Isóceles!')
elif a < b + c and c < a + b  and b < c + a and a != b != c:
    print('Triângulo Escaleno!')
else:
    print('Não pode existir triângulo!')
