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
fenetre = pygame.display.set_mode((640, 480))

perso = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png")
perso2 = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png")
perso2.setPositionInit(100,100)
perso3 = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png")
perso3.setPositionInit(148,100)

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
		menu = Menu(fenetre)
		menu.open_menu()
	if keys[K_RIGHT]:
		if perso.position_perso.colliderect(perso2.setPosition(-3,0))!=1:
			print "collision droite"
			perso.deplacer("droite", fenetre)
	if keys[K_LEFT]:
		if perso.position_perso.colliderect(perso2.setPosition(3,0))!=1:
			print "collision gauche"
			perso.deplacer("gauche", fenetre)
	if keys[K_UP]:
		if perso.position_perso.colliderect(perso2.setPosition(0,3))!=1:
			print "collision haut"
			perso.deplacer("haut", fenetre)
	if keys[K_DOWN]:
		if perso.position_perso.colliderect(perso2.setPosition(0,-3))!=1: 
			print "collision bas"
			perso.deplacer("bas", fenetre)




	


	# Remplace le fond
	fenetre.fill(pygame.Color("Black"))
	fenetre.blit(tile[2][5], (0, 0))
	fenetre.blit(tile[5][4], (48, 48))
	fenetre.blit(tile[5][4], (96, 96))
	fenetre.blit(tile[5][4], (144, 144))
	fenetre.blit(tile[5][4], (192, 192))
	fenetre.blit(tile[5][4], (240, 240))
	fenetre.blit(perso.direction, perso.position_perso)
	fenetre.blit(perso2.direction, perso2.position_perso)
	fenetre.blit(perso3.direction, perso3.position_perso)
	pygame.display.flip()
