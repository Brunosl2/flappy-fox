#define condições 
import pygame
from pygame.locals import *

pygame.display.set_caption('FlappyFox')
LARGURA = 500
ALTURA = 600
VELOCIDADE = 10
GRAVIDADE = 1
VEL_JOGO = 10 
LARGURA_CHAO = 2 * LARGURA
ALTURA_CHAO = 100
LARGURA_CANO = 80
ALTURA_CANO = 500
ESPACO_CANO = 200

#define a tela de fundo
BACKGROUND = pygame.image.load('insper.png')
#transforma para o tamanho da tela
BACKGROUND = pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA))
