mai = men = 0
listanum = []
for c in range (0, 5):
    listanum.append(int(input(f'Digite um número para posição {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'Você digitou os valores {listanum}')
print(f'O menor número digita foi: {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print(f'O maior número digitado foi: {mai} nas posições ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
