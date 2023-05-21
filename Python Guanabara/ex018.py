from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, s))
c = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, c))
t = tan(radians(ang))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, t))
