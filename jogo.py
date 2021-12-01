#importando as bibliotecas  
import pygame
from pygame.locals import *
import random
from inicial import *
from classes import *


#inicia o jogo e configurações iniciais
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))

#Cria grupos
raposa_group = pygame.sprite.Group()
chao_group = pygame.sprite.Group()
cano_group = pygame.sprite.Group()

#para mostrar a raposa
raposa = Raposa()
raposa_group.add(raposa)

#para o chão ficar passando (sensação de andar)
for i in range(2):
    chao = Chao(LARGURA_CHAO * i)
    chao_group.add(chao)

#para os canos ficarem aparecendo na tela com um espaço entre 
for i in range(2):
    canos = canos_aleatorios(LARGURA * i + 800)
    cano_group.add(canos[0])
    cano_group.add(canos[1])

#dá um nome mais fácil para colocar o fps
clock = pygame.time.Clock()



while True:
    #define FPS
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


        #para a raposa pular
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                raposa.pulo()
    
    #mostra o fundo
    tela.blit(BACKGROUND, (0,0))

    #condições -> caso a raposa colida com o cano ou com o chão
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

    #movimentação das classes
    raposa_group.update()
    chao_group.update()
    cano_group.update()
    
    #desenha o que irá aparecer na tela
    raposa_group.draw(tela)
    cano_group.draw(tela)
    chao_group.draw(tela)
    
    

    #atualiza a tela
    pygame.display.update()

    if pygame.sprite.groupcollide(raposa_group, chao_group, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(raposa_group, cano_group, False, False, pygame.sprite.collide_mask):
        break