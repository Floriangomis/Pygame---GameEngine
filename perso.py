import pygame
from pygame.locals import *

class Perso(object):

	def __init__(self, img_droite, img_gauche, img_haut, img_bas, positionX, positionY, fenetre):
		super(Perso, self).__init__()

		self.screen = fenetre

		self.currentTile = 0
		self.nextTitle = 0

		# On charge les images pour les differentes positions
		self.img_droite = pygame.image.load(img_droite).convert_alpha()
		self.img_gauche = pygame.image.load(img_gauche).convert_alpha()
		self.img_haut = pygame.image.load(img_haut).convert_alpha()
		self.img_bas = pygame.image.load(img_bas).convert_alpha()

		#imageDirection par defaut
		self.imageDirection = self.img_droite

		#Position du personnage en cases et en pixels
		self.rectPerso = self.imageDirection.get_rect()
		self.rectPerso = self.rectPerso.move(positionX, positionY)

	def event(self, tileMap):
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0

		keys = pygame.key.get_pressed()

		#if tileMap.getTile(self.rectPerso.top+3, self.rectPerso.left).passable != False:            ->>> Collision Test 		
		if keys[K_RIGHT]:
			self.imageDirection = self.img_droite 
			if tileMap.getTile(self.rectPerso.top, self.rectPerso.left+33).passable == True and tileMap.getTile(self.rectPerso.top+30, self.rectPerso.left+33).passable == True:
				self.rectPerso = self.rectPerso.move(3,0)
				self.screen.blit(self.imageDirection, self.rectPerso)
		if keys[K_LEFT]:
			self.imageDirection = self.img_gauche
			if tileMap.getTile(self.rectPerso.top, self.rectPerso.left-3).passable == True and tileMap.getTile(self.rectPerso.top+30, self.rectPerso.left-3).passable == True:
				self.rectPerso = self.rectPerso.move(-3,0)
				self.screen.blit(self.imageDirection, self.rectPerso)
		if keys[K_UP]:
			self.imageDirection = self.img_haut
			if tileMap.getTile(self.rectPerso.top-3, self.rectPerso.left).passable == True and tileMap.getTile(self.rectPerso.top-3, self.rectPerso.left+30).passable == True:
				self.rectPerso = self.rectPerso.move(0,-3)
				self.screen.blit(self.imageDirection, self.rectPerso)
		if keys[K_DOWN]:
			self.imageDirection = self.img_bas
			if tileMap.getTile(self.rectPerso.top+33, self.rectPerso.left).passable == True and tileMap.getTile(self.rectPerso.top+33, self.rectPerso.left+30).passable == True:
				self.rectPerso = self.rectPerso.move(0,3)
				self.screen.blit(self.imageDirection, self.rectPerso)

		self.screen.blit(self.imageDirection, self.rectPerso)