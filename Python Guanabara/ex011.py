larg = float(input('Digite a largura de uma parede em metros: '))
alt = float(input('Digite a altura de uma parede em metros: '))
área = larg * alt
print('Sua parede tem a dimenção de \033[33m{}\033[mx\033[33m{}\033[m e sua área é de \033[36m{}m².\033[m'.format(larg, alt, área))
print('Para pintar essa parede, você precisará de \033[32m{}l\033[m de tinta'.format(área/2))
#cada 1l de tinta pinta uma área de 2m²