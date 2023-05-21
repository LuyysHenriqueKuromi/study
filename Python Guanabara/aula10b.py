n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
#condição composta
if m >= 6.0:
    print('Sua média foi boa! PARABÊNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
#condição simplificada
print('PARABÊNS' if m >= 6.0 else 'ESTUDE MAIS')
