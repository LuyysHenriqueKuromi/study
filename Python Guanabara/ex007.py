nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('A média entre \033[33m{:.1f}\033[m e \033[33m{:.1f}\033[m é igual a \033[32m{:.1f}\033[m'.format(nota1, nota2, (nota1+nota2)/2))
