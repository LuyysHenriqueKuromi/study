num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
for c in range(0, 11):
    r = c * num
    print(f'\033[33m{num}\033[m x \033[33m{c:2}\033[m = \033[32m{r}\033[m')
print('-'*12)
