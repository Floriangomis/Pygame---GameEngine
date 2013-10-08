import pygame
import sys, os
from tileset import tileSet
from tilemap import tileMap
from cursor import Cursor
from map import Map
from menu import Menu
import settings as settings
from perso import Perso
from pygame.locals import *

# Initialisation de l objet Pygame et Creation de la surface sur laquelle on va dessiner les element
pygame.init()
fenetre = pygame.display.set_mode((800, 600))
#Creation des perso Pj et Pnj
perso = Perso("./ressources/images/dk_droite.png","./ressources/images/dk_gauche.png","./ressources/images/dk_haut.png","./ressources/images/dk_bas.png", 200, 100, fenetre)


#On charge la carte en memoire puis on cree un tableau qui contient les case de l image.
tileSet = tileSet("./ressources/images/tileset.png")
tileSet.load_tile_table(48,48)
dicoTile = tileSet.genererDicoTile()
# Creation du tableau qui represente la map
map = Map('level.lvl')
Matrix = map.getMyArrayMap()
# Creation de l objet TileMap ou on va gerer le rendu de la map
tileMap = tileMap(Matrix, dicoTile, fenetre)


#LA BOUCLE PRINCIPALE DEMARRE ICI 
continuer = 1
mon_horloge = pygame.time.Clock()
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

	keys = pygame.key.get_pressed()

	if keys[K_ESCAPE]:
		menu = Menu(fenetre)
		menu.open_menu()


	# Remplace le fond
	fenetre.fill(pygame.Color("Black"))
	#Rendu de la map
	tileMap.mapRender()
	#On gere le Perso Ici (Mouvement et affichage a l ecran)
	perso.event()




	pygame.display.flip()
	mon_horloge.tick(60)
