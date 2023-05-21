n = int(input('Digite um número: '))
print('O dobro de {} vale \033[4;36m{}\033[m \nO triplo de {} vale \033[4;34m{}\033[m \nE a raiz quadrada de {} vale \033[4;35m{:.2f}\033[m'.format(n, n*2, n, n*3, n, n**(1/2)))
