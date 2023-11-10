print('Emprestimo Bancário!')
print('-'*20)

vc = float(input('Valor da casa: '))
s = float(input('Salário: '))
a = int(input('Anos para pagar: '))

m = a * 12    #transformando anos para mêses
p = vc / m    #valor das parcelas por mês
minimo = s * 30/100   #30% do salário

print('O valor a ser pago por mês é R${:.2f}!'.format(p))


if p > minimo:   #checado se o emprestimo é possível
    print('Emprestimo negado!')
else:
   print('Emprestimo aprovado!')

