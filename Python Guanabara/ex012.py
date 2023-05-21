p = float(input('Qual o preço do produto? R$'))
print('O produto que custava \033[33mR${:.2f}\033[m, com um desconto de \033[36m5%\033[m vai valer \033[32mR${:.2f}\033[m'.format(p, p*0.95))
