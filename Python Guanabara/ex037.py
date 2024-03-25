num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÉRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL á igual a {hex(num)[2:]}')
else:
    print('Opção invalida. Tente novamente.')
