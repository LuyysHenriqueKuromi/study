#frase = str(input("Digite uma frase: "))
#frase = 'MARCOS'
frase = 'ARARA RARA'
#            01234  0123
# ARARARARA
# 0123456789

frase = frase.replace(' ','')

num = len(frase)

frase_list_normal = []

n1 = 0
m1 = 1

for b in range(0, num):
    print(frase[n1: m1])
    n1 += 1
    m1 += 1
    frase_list_normal.append(frase[b])
print(frase_list_normal)

frase_list_reverse = []

n2 = num - 1
m2 = num

for c in range(num -0, 0, -1):
    print(frase[n2: m2])
    n2 -= 1
    m2 -= 1
    frase_list_reverse.append(frase[c-1])
print(frase_list_reverse)

if frase_list_normal == frase_list_reverse:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
