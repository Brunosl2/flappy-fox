#importando as bibliotecas  
import pygame
from pygame.locals import *
import random

#define tamanho da tela
LARGURA = 400
ALTURA = 600
VELOCIDADE = 10
GRAVIDADE = 1
VEL_JOGO = 10 

LARGURA_CHAO = 2 * LARGURA
ALTURA_CHAO = 100

LARGURA_CANO = 80
ALTURA_CANO = 500

ESPACO_CANO = 200

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
class Canos(pygame.sprite.Sprite):

    def __init__(self, inverted, x, tamanho_cano):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('pipe-red.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (LARGURA_CANO, ALTURA_CANO))

        self.rect = self.image.get_rect()
        self.rect[0] = x 

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - tamanho_cano)
        else:
            self.rect[1] = ALTURA - tamanho_cano


        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.rect[0] -= VEL_JOGO



class Chao(pygame.sprite.Sprite):
    
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('base.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (LARGURA_CHAO, ALTURA_CHAO))

        self.rect = self.image.get_rect()
        self.rect[1] = ALTURA - ALTURA_CHAO
        self.rect[0] = x

    def update(self):

        self.rect[0] -= VEL_JOGO

def fora_da_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def canos_aleatorios(x):
    tamanho = random.randint(100, 300)
    cano = Canos(False, x, tamanho)
    cano_invertido = Canos(True, x,ALTURA - tamanho - ESPACO_CANO)
    return (cano, cano_invertido)


#inicia o jogo e configurações iniciais
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))

#define a tela de fundo
BACKGROUND = pygame.image.load('background-day.png')
#transforma para o tamanho da tela
BACKGROUND = pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA))

#para mostrar a raposa no jogo
raposa_group = pygame.sprite.Group()
raposa = Raposa()
raposa_group.add(raposa)

chao_group = pygame.sprite.Group()

for i in range(2):
    chao = Chao(LARGURA_CHAO * i)
    chao_group.add(chao)



cano_group = pygame.sprite.Group()
for i in range(2):
    canos = canos_aleatorios(LARGURA * i + 800)
    cano_group.add(canos[0])
    cano_group.add(canos[1])
#dá um nome mais fácil para colocar o fps
clock = pygame.time.Clock()



while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                raposa.pulo()

    #mostra o fundo
    tela.blit(BACKGROUND, (0,0))

    if fora_da_tela(chao_group.sprites()[0]):
        chao_group.remove(chao_group.sprites()[0])

        novo_chao = Chao(LARGURA_CHAO - 20)
        chao_group.add(novo_chao)
    if fora_da_tela(cano_group.sprites()[0]):
        cano_group.remove(cano_group.sprites()[0])
        cano_group.remove(cano_group.sprites()[0])

        canos = canos_aleatorios(LARGURA * 2)

        cano_group.add(canos[0])
        cano_group.add(canos[1])

    raposa_group.update()
    chao_group.update()
    cano_group.update()
    
    raposa_group.draw(tela)
    cano_group.draw(tela)
    chao_group.draw(tela)
    
    

    #atualiza a tela
    pygame.display.update()

    if pygame.sprite.groupcollide(raposa_group, chao_group, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(raposa_group, cano_group, False, False, pygame.sprite.collide_mask):
        break