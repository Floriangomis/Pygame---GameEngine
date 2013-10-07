import pygame
import sys, os
from tilemap import tileMap
from cursor import Cursor
from menu import Menu
import settings as settings
from perso import Perso
from pygame.locals import *

pygame.init()

BLACK = 0, 0, 0
fenetre = pygame.display.set_mode((800, 600))

#Creation des perso Pj et Pnj
perso = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png", 0, 0)
perso2 = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png",100,100)
perso3 = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png",200,100)

liste = [perso2, perso3]

#On charge la carte en memoire puis on cree un tableau qui contient les case de l image.
tileMap = tileMap("./ressources/images/tileset.png")
tile = tileMap.load_tile_table(48,48)

continuer = 1
mon_horloge = pygame.time.Clock()

# On recupere dans le fichier Level le niveau puis on construit un tableau a deux dimension
Matrix = [[0 for x in xrange(36)] for x in xrange(16)] 
h=0
f = open('level.lvl','r')
for line in f:
	h = h+1
	for x in xrange(0,len(line)):
		if line[x] == '0' or line[x] == '1':
			Matrix[h][x] = line[x]
f.close()


while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		menu = Menu(fenetre)
		menu.open_menu()

	if keys[K_RIGHT]:
		if perso.position_perso.colliderect(perso2.setPosition(-3,0))!=1:
			perso.deplacer("droite", fenetre)
	if keys[K_LEFT]:
		if perso.position_perso.colliderect(perso2.setPosition(3,0))!=1:
			perso.deplacer("gauche", fenetre)
	if keys[K_UP]:
		if perso.position_perso.colliderect(perso2.setPosition(0,3))!=1:
			perso.deplacer("haut", fenetre)
	if keys[K_DOWN]:
		if perso.position_perso.colliderect(perso2.setPosition(0,-3))!=1: 
			perso.deplacer("bas", fenetre)

	# Remplace le fond
	fenetre.fill(pygame.Color("Black"))

	for width in range(len(Matrix)):
		for height in range(len(Matrix[width])):
			if Matrix[width][height] == '0':
				fenetre.blit(tile[1][4], (height*48, (width-1)*48))
			if Matrix[width][height] == '1':
				fenetre.blit(tile[3][4], (height*48, (width-1)*48))

	fenetre.blit(perso.direction, perso.position_perso)
	fenetre.blit(perso2.direction, perso2.position_perso)
	fenetre.blit(perso3.direction, perso3.position_perso)

	pygame.display.flip()
	mon_horloge.tick(60)
