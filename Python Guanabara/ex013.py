s = float(input('Qual é o salário do funcionário? R$'))
print('Um funcionário que ganhava \033[33mR${:.2f}\033[m, com \033[36m15%\033[m de aumento, passa a receber \033[32mR${:.2f}'.format(s, s*1.15))
