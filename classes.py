import pygame
from pygame.locals import *
import random
from inicial import *


#criando classes para definir imagens e movimentos
class Raposa(pygame.sprite.Sprite):

    #define os movimentos da raposa
    def __init__(self):
        #inicializa o sprite
        pygame.sprite.Sprite.__init__(self)

        self.speed = VELOCIDADE

        self.image = pygame.image.load('raposa.png').convert_alpha() #adiciona a imagem e interpreta pixel transparente
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA / 2
        self.rect[1] = ALTURA / 2


    def update(self):
        #atualizar altura
        self.rect[1] += self.speed
        self.speed += GRAVIDADE

    def pulo(self):
        self.speed = - VELOCIDADE

#classe dos canos para demonstrar as imagens
class Canos(pygame.sprite.Sprite):
    def __init__(self, inverted, x, tamanho_cano):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('canos.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_CANO, ALTURA_CANO))

        self.rect = self.image.get_rect()
        self.rect[0] = x 

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - tamanho_cano)
        else:
            self.rect[1] = ALTURA - tamanho_cano


        self.mask = pygame.mask.from_surface(self.image)

    #passagems dos canos velocidade definida
    def update(self):
        self.rect[0] -= VEL_JOGO


#classe chão para adicionar as imagens
class Chao(pygame.sprite.Sprite):
    
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('base.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (LARGURA_CHAO, ALTURA_CHAO))

        self.rect = self.image.get_rect()
        self.rect[1] = ALTURA - ALTURA_CHAO
        self.rect[0] = x

    #passagem do chão
    def update(self):
        self.rect[0] -= VEL_JOGO

#caso bata fora da tetla
def fora_da_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

#para os canos aparecerem de forma aleatória
def canos_aleatorios(x):
    tamanho = random.randint(100, 300)
    cano = Canos(False, x, tamanho)
    cano_invertido = Canos(True, x,ALTURA - tamanho - ESPACO_CANO)
    return (cano, cano_invertido)
