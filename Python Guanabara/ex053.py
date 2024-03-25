#f = str(input('Digite uma frase: '))
#frase = 'ARARA RARA'
frase = 'MARCOS '
#frase = 'YFJI GATO'
frase = frase.replace(' ','')

frase_list_normal = []
num = len(frase)

n1 = 0
m1 = 1

n2 = num -1
m2 = num

for c in range(0, num):
    print(frase[n1:m1])
    n1 = n1 + 1
    m1 = m1 + 1
    frase_list_normal.append(frase[c])
print(frase_list_normal)

print('=-' * 15)

frase_list_normal_r = []

for b in range(num -0, 0, -1):
    print(frase[n2:m2])
    n2 -= 1
    m2 -= 1
    frase_list_normal_r.append(frase[b-1])
print(frase_list_normal_r)

if frase_list_normal == frase_list_normal_r:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')

# ARARA RARA
# 01234 0123
# 01234 5678
# 87654 3210