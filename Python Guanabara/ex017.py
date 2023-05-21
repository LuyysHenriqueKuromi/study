import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hipotenusa = math.sqrt(pow(co,2)+pow(ca,2))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(pow(co,2)+pow(ca,2))))

h = ((co**2)+(ca**2))**0.5
print('A hipotenusa vai medir {:.2f}'.format(h))

#forma que o Guanabara passou na resolução, que teria feito em 10 seg se ele tivesse explicado o que cada merde de comando do math faz

#from math import hypor
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#apagar o "math." e deixar só o hypot