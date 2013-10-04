import pygame
import sys, os
from tilemap import tileMap
from perso import Perso
from pygame.locals import *

pygame.init()

BLACK = 0, 0, 0
fenetre = pygame.display.set_mode((640, 480))

perso = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png")

tileMap = tileMap("./ressources/images/tileset.png")
tile = tileMap.load_tile_table(48,48)

continuer = 1

mon_horloge = pygame.time.Clock()

while continuer:
	mon_horloge.tick(60)

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		continuer = 0
	if keys[K_RIGHT]:
		perso.deplacer("droite", fenetre)
	if keys[K_LEFT]:
		perso.deplacer("gauche", fenetre)
	if keys[K_UP]:
		perso.deplacer("haut", fenetre)
	if keys[K_DOWN]:
		perso.deplacer("bas", fenetre)

	# Remplace le fond
	fenetre.fill(BLACK)

	fenetre.blit(perso.direction, perso.position_perso)

	pygame.display.flip()
