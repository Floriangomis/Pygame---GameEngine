import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond,(0,0))

perso = pygame.image.load("perso.png").convert_alpha()
fenetre.blit(perso, (100,200))

pygame.display.flip()

continuer = 1

while continuer:
        for event in pygame.event.get():
                if event.type == QUIT:
                        continuer = 0
