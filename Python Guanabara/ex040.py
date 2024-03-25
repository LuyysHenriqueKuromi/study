nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2)/2
print(f'Tirando {nota_1:.1f} e {nota_2:.1f}, a média foi {media:.1f}')

print('O aluno está', end=' ')
if media < 5.0:
    print('\033[31mREPROVADO')
elif 5.0 <= media <7.0:
    print('de \033[33mRECUPERAÇÃO')
elif media >= 7.0:
    print('\033[32mAPROVADO')
