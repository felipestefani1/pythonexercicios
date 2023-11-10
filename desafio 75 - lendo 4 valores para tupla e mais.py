n = int(input('1o valor: ')), int(input('2o valor: ')), int(input('3o valor: ')), int(input('4o valor: '))
print(f'Você digitou {n}')
print(f'O 9 foi digitado {n.count(9)} vezes.')
if 3 in n:
  print(f'O 3 apareceu na posição {n.index(3)+1}')
else:
  print('O número 3 não apareceu')
print(f'Os valores pares digitados foram ', end='')
for num in n:
  if num % 2 == 0:
    print(num, end='')

