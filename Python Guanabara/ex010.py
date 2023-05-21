n = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Considerando que R$3.27 = US$1.00')
print('Com exatamente \033[32mR${:.2f}\033[m você pode comprar \033[32mUS${:.2F}\033[m'.format(n, n/3.27))
#US$1.00=R$3.27
#US$2.00=R$6.54
#US$3.00=R$9.81
#US$4.00=R$13.08