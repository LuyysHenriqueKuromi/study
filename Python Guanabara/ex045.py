from random import choice
from time import sleep

lista = [1, 2, 3]
computador = choice(lista) # Faz o computador escolher
print('-=-' * 20)
print('Vamos jogar Jokenpô. Escolha entre pedra, papel ou tesoura e tente me ganhar')
print('-=-' * 20)
print('Digiteo número correspondente. Pedra(1); Pepel(2); Tesoura(3)')
jogador = int(input('Escolha: ')) # Jogador escolhe
print('PROCESSANDO...')
sleep(3)

if jogador == 1:
    if computador == 1:
        print('Opa parece que empatamos')
    elif computador == 2:
        print('AH AH, você perdeu e eu venci... ez UwU')
    elif computador == 3:
        print('Você venceu, parabens, aqui o meu singelo GG')
elif jogador == 2:
    if computador == 1:
        print('Você venceu, parabens, aqui o meu singelo GG')
    elif computador == 2:
        print('Opa parece que empatamos')
    elif computador == 3:
        print('AH AH, você perdeu e eu venci... ez UwU')
elif jogador == 3:
    if computador == 1:
        print('AH AH, você perdeu e eu venci... ez UwU')
    elif computador == 2:
        print('Você venceu, parabens, aqui o meu singelo GG')
    elif computador == 3:
        print('Opa parece que empatamos')
elif jogador <= 4:
    print('Você é burro por acaso?')
