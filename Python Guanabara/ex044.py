print(f'='*10,'LOJA DO GROSSO', '='*10)
produt = float(input('Digite o valor do produto em R$'))
print('''Forma de pagamento:
[ 1 ] para à vista dinheiro/cheque
[ 2 ] para à vista no cartão
[ 3 ] para 2x no cartão
[ 4 ] para 3x ou mais no cartão''')
pagamento = int(input('Qual você gostaria de escolher? '))

if pagamento == 1:
    total = produt * 0.90
    print(f'Você escolheu o pegamento à vista dinheiro/cheque. Sua compra de R${produt:.2f} terá o valor final de R${total:.2f}')
elif pagamento == 2:
    total = produt * 0.95
    print(f'Você escolheu o pagamento à vista no cartão. Sua compra de R${produt:.2f} terá o valor final de R${total:.2f}')
elif pagamento == 3:
    total = produt
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
    print(f'Você escolheu o pagamento para 2x no cartão. Sua compra de R${produt:.2f} terá o valor final de R${total:.2f}')
elif pagamento == 4:
    total = produt * 1.20
    quant_parc = int(input('Em quantas parcelas? '))
    parcela = total / quant_parc
    print(f'Sua compra será parcelada em {quant_parc}x de R${parcela:.2f} COM JUROS')
    print(f'Você escolheu o pagamento para 3x ou mais no cartão. Sua compra de R${produt:.2f} terá o valor final de R${total:.2f}')
else:
    print('OPÇÃO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!')