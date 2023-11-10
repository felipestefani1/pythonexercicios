s = 0
num = 0
for c in range(0, 6):
    num += 1
    n = int(input('Digite o número {} :'.format(num)))
    if n % 2 == 0:
        s += n
print(s)
