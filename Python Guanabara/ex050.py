soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
    else:
        soma = soma + 0
print(f'Você informou {cont} números PARES e a soma foi {soma}')
