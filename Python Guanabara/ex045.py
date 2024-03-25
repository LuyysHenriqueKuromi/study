from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
print('-=-' * 20)
print('Vamos jogar Jokenpô. Escolha entre pedra, papel ou tesoura e tente me ganhar')
print('-=-' * 20)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Escolha: '))
print('PROCESSANDO...')
sleep(3)

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

if jogador == 1:
    if computador == 1:
        print('Opa parece que empatamos')#E
    elif computador == 2:
        print('AH AH, você perdeu e eu venci... ez UwU')#P
    elif computador == 3:
        print('Você venceu, parabens, aqui o meu singelo GG')#V
elif jogador == 2:
    if computador == 1:
        print('Você venceu, parabens, aqui o meu singelo GG')#V
    elif computador == 2:
        print('Opa parece que empatamos')#E
    elif computador == 3:
        print('AH AH, você perdeu e eu venci... ez UwU')#P
elif jogador == 3:
    if computador == 1:
        print('AH AH, você perdeu e eu venci... ez UwU')#P
    elif computador == 2:
        print('Você venceu, parabens, aqui o meu singelo GG')#V
    elif computador == 3:
        print('Opa parece que empatamos')#E
else:
    print('Você é burro por acaso? >:( OPÇÃO INVALIDA, TENTE NOVAMENTE')
    