maior_p = 0
menor_p = 1000

for c in range(1, 6):
    peso = int(input(f'Digite o peso da {c}° pessoa: '))
    if peso > maior_p:
        maior_p = peso
    elif peso < menor_p:
        menor_p = peso
        
print(f'O maior peso foi {maior_p}')
print(f'O menor peso foi {menor_p}')
