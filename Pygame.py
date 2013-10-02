import pygame
import sys, os
from perso import Perso
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

fond = pygame.image.load("./ressources/images/background.jpg").convert()

perso = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png")

continuer = 1

mon_horloge = pygame.time.Clock()# On cree l horloge 

pygame.key.set_repeat(400, 30)
while continuer:
	mon_horloge.tick(60)

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		continuer = 0
	if keys[K_RIGHT]:
		perso.deplacer("droite")
	if keys[K_LEFT]:
		perso.deplacer("gauche")
	if keys[K_UP]:
		perso.deplacer("haut")
	if keys[K_DOWN]:
		perso.deplacer("bas")


	fenetre.blit(fond,(0,0))
	fenetre.blit(perso.direction, (perso.x, perso.y))
	pygame.display.flip()
