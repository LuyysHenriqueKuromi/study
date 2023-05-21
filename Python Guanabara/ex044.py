produt = float(input('Digite o valor do produto em R$'))
print('Forma de pagamento:')
print('1 para à vista dinheiro/cheque\n2 para à vista no cartão\n3 para 2x no cartão\n4 para 3x ou mais no cartão')
pagamento = int(input('Qual você gostaria de escolher? '))

if pagamento == 1:
    produt = produt * 0.90
    print('Você escolheu o pegamento à vista dinheiro/cheque. O preço do produto é de R${}'.format(produt))
elif pagamento == 2:
    produt = produt * 0.95
    print('Você escolheu o pagamento à vista no cartão. O preço do produto é de R${}'.format(produt))
elif pagamento == 3:
    print('Você escolheu o pagamento para 2x no cartão. O preço do produto é de R${}'.format(produt))
elif pagamento == 4:
    produt = produt * 1.20
    print('Você escolheu o pagamento para 3x ou mais no cartão. O preço do produto é de R${}'.format(produt))