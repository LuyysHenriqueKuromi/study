n = int(input('Digite um número: '))
quant = 0

for c in range(1, n + 1):
    if n % c == 0:
        print(f'c: {c}')
        quant = quant + 1

print(quant)
if quant == 2:
    print(f'O número {n} É PRIMO')
elif quant > 2 or quant < 2:
    print(f'O número {n} NÃO É PRIMO')
