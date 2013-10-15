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

		#Direction par defaut
		self.direction = self.img_droite

		#Position du personnage en cases et en pixels
		self.position_perso = self.direction.get_rect()
		self.position_perso = self.position_perso.move(positionX, positionY)

	def event(self, tileMap):
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0

		keys = pygame.key.get_pressed()

		if keys[K_RIGHT]:
			self.direction = self.img_droite
			if tileMap.getTile(self.currentTile.rect[0][0], self.currentTile.rect[0][1]).passable == True:
				self.position_perso = self.position_perso.move(3,0)
				self.screen.blit(self.direction, self.position_perso)
		if keys[K_LEFT]:
			self.direction = self.img_gauche
			if tileMap.getTile(self.currentTile.rect[0][0], self.currentTile.rect[0][1]).passable == True:
				self.position_perso = self.position_perso.move(-3,0)
				self.screen.blit(self.direction, self.position_perso)
		if keys[K_UP]:
			self.direction = self.img_haut
			if tileMap.getTile(self.currentTile.rect[0][0], self.currentTile.rect[0][1]).passable == True:
				self.position_perso = self.position_perso.move(0,-3)
				self.screen.blit(self.direction, self.position_perso)
		if keys[K_DOWN]:
			self.direction = self.img_bas
			if tileMap.getTile(self.currentTile.rect[0][0], self.currentTile.rect[0][1]).passable == True:
				self.position_perso = self.position_perso.move(0,3)
				self.screen.blit(self.direction, self.position_perso)
		#Met a jour la position du perso
		self.screen.blit(self.direction, self.position_perso)

	def testTile(self, tileMap):
		self.currentTile = tileMap.getTile(self.position_perso.left, self.position_perso.top)
			#self.currentTile.getSurface().fill((255,255,255,255))
			#tileMap.getTile(self.currentTile.rect[0][0]+48, self.currentTile.rect[0][1]).getSurface().fill((255,255,255,255))
		self.event(tileMap)


	def setPosition(self, positionX, positionY):
		return self.position_perso.move(positionX, positionY)

		


		

