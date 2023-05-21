a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = int(input('Digite a quantidade de termos: '))
m = 0

for c in range(1, t + 1):
    pa = a1 + m * r
    m = m + 1
    print(pa)
