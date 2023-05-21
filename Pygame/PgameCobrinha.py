#importar todos os modulos
import pygame
from pygame.locals import *
from sys import exit
from random import randint

#iniciar os modulos do pygame
pygame.init()

#musica de fundo
pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('Pygame/BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)

#som da moeda
barulho_colisão = pygame.mixer.Sound('Pygame/smw_coin.wav')
barulho_colisão.set_volume(0.3)

#tamanho da janela
largura = 640
altura = 480

#onde a cobra vai nascer na tela
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

#velocidade de movimantação da cobra
velocidade = 10
x_controle = velocidade
y_controle = 0

#posições de onde a maçâ vai nascer aleatoriamente
x_maca = randint(40,600)
y_maca = randint(50,430)

#marca de pontuação
pontos = 0
fonte = pygame.font.SysFont('arial',40, True, True)

#tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

#função de desenhar e crescer a cobra na tela
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

#função de reiniciar o jogo quando perder
def reinicia_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

#loop
while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle            

    #movimento da cobra
    '''''
    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 20
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 20
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 20'''

    #
    tela.blit(texto_formatado, (450,40))

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    
    #se a cobra colidir com a maçã a maçã muda a posição, ganha +1 ponto, faz som e a cobra cresce em +1
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos = pontos + 1
        barulho_colisão.play()
        comprimento_inicial = comprimento_inicial + 1
    
    #armazena os valores de X e Y
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    #mensagem de game over
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()
        
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reinicia_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
            
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0    
                    
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    #função dentro do loop    
    aumenta_cobra(lista_cobra)

    pygame.display.update()        