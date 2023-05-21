nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2)/2
print('Sua média foi {}'.format(media))

if media < 5.0:
    print('\033[31mREPROVADO')
elif 5.0 <= media <7.0:
    print('\033[33mRECUPERAÇÃO')
elif media > 6.9:
    print('\033[32mAPROVADO')
