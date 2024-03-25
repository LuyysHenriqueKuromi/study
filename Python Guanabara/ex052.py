n = int(input('Digite um número inteiro: '))
quant = 0

print('Ele é divisivel por:')
for c in range(1, 10):
    if n % c == 0:
        print(c)
        quant += 1

if quant <= 2:
    print(f'O número {n} É  PRIMO')
else:
    print(f'O número {n} NÃO É PRIMO')
