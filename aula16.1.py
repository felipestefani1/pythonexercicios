#num = [1, 2, 4, 5]
#num[2] = 7
#num.append(8)
#num.sort(reverse=True)
#num.insert(1, 50)
#num.remove(1)
#print(num)
#print(len(num))

valores = list()
valores.append(3)
valores.append(6)
valores.append(9)
#for c, v in enumerate(valores):
    #print(f'Na posição {c} encontrei o valor {v}!')

for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

print (enumerate(valores))