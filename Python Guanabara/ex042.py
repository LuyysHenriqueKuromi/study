r_a = float(input('Primeiro segmento: '))
r_b = float(input('Segundo segmento: '))
r_c = float(input('Terceiro segmento: '))

if r_a + r_b > r_c and r_a + r_c > r_b and r_b + r_c > r_a:
    print('Os segmentos acima PODEM FORMAR triãngulo', end='')
    if r_a == r_b == r_c:
        print('EQUILÁTERO')
    elif r_a != r_b != r_c != r_a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triãngulo')