num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print(f'\033[33m{num}\033[m x \033[33m{c:2}\033[m = \033[32m{num*c:2}\033[m')
print('-' * 12)
