from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu escolhi o número {} não o número {}!'.format(computador, jogador))
