frase = 'UM LUGAR ESPECIAL CHAMADO USAHESE'
frase = frase.replace(' ', '')

frase_list_normal = []
num = len(frase)

print(num)
print(frase.split())

for c in range(0, num):
    frase_list_normal.append(frase[c])
print(frase_list_normal)

frase_list_ravers = []

for n in range( num, 0, -1):
    frase_list_ravers.append(frase[n-1])
print(frase_list_ravers)

if frase_list_normal == frase_list_ravers:
    print('São palindromos')
else:
    print('Não são palindromos')
