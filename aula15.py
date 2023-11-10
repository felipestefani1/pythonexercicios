#n = 0
#while n <= 10:
#    print(n, '...', end='')
#    n += 1
#print('Fim')

n = s = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')
