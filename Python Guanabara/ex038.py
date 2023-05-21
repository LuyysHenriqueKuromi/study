n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
maior = n1
if n1 < n2:
    maior = n2
    print('O maior valor é {}'.format(maior))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('O maior valor é {}'.format(maior))
