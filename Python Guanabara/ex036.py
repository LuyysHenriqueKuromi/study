casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você deseja pagar? '))

prestação = casa / (anos * 12)
minimo = salario * 0.30

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))

if prestação <= minimo:
    print('Empréstimo APROVADO!')

else:
    print('Empréstimo NEGADO!')