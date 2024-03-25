frase = 'YFJI GATO'
frase = frase.replace(' ','')

frase_list_normal = []

num = len(frase)

n2 = num
m2 = num + 1

for b in range(num-1, -1, -1):
    print(frase[n2:m2])
    n2 = n2 - 1
    m2 = m2 - 1
    frase_list_normal.append(frase[b-1])
print(frase_list_normal)
