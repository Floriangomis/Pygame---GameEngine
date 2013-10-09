import pygame
from pygame.locals import *

class Perso(object):

	def __init__(self, img_droite, img_gauche, img_haut, img_bas, positionX, positionY, fenetre):
		super(Perso, self).__init__()

		self.screen = fenetre

		self.currentTile = 0

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

	def event(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0

		keys = pygame.key.get_pressed()

		if keys[K_RIGHT]:
			self.direction = self.img_droite
			self.position_perso = self.position_perso.move(3,0)
			self.screen.blit(self.direction, self.position_perso)
		if keys[K_LEFT]:
			self.direction = self.img_gauche
			self.position_perso = self.position_perso.move(-3,0)
			self.screen.blit(self.direction, self.position_perso)
		if keys[K_UP]:
			self.direction = self.img_haut
			self.position_perso = self.position_perso.move(0,-3)
			self.screen.blit(self.direction, self.position_perso)
		if keys[K_DOWN]:
			self.direction = self.img_bas
			self.position_perso = self.position_perso.move(0,3)
			self.screen.blit(self.direction, self.position_perso)
		
		#Met a jour la position du perso
		self.screen.blit(self.direction, self.position_perso)

	def testTile(self, perso, tileMap):
		self.currentTile = tileMap.getTile(self.position_perso.left, self.position_perso.top)
		print self.currentTile.rect
		print perso.position_perso
		if perso.position_perso.colliderect(self.currentTile.rect) and self.currentTile.passable == True:
			self.currentTile.getSurface().fill((255,255,255,255))
			print "On passe"
		


		

