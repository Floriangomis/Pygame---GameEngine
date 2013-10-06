import pygame
from pygame.locals import *

class Perso(object):

	def __init__(self, img_droite, img_gauche, img_haut, img_bas):
		super(Perso, self).__init__()

		# On charge les images pour les differentes positions
		self.img_droite = pygame.image.load(img_droite).convert_alpha()
		self.img_gauche = pygame.image.load(img_gauche).convert_alpha()
		self.img_haut = pygame.image.load(img_haut).convert_alpha()
		self.img_bas = pygame.image.load(img_bas).convert_alpha()

		#Direction par defaut
		self.direction = self.img_droite 

		#Position du personnage en cases et en pixels
		self.position_perso = self.direction.get_rect()


	def deplacer(self, direction, fenetre):
		if direction == "droite":
			self.direction = self.img_droite
			self.position_perso = self.position_perso.move(3,0)
			fenetre.blit(self.direction, self.position_perso)


		if direction == "gauche":
			self.direction = self.img_gauche
			self.position_perso = self.position_perso.move(-3,0)
			fenetre.blit(self.direction, self.position_perso)


		if direction == "haut":
			self.direction = self.img_haut
			self.position_perso = self.position_perso.move(0,-3)
			fenetre.blit(self.direction, self.position_perso)

		if direction == "bas":
			self.direction = self.img_bas
			self.position_perso = self.position_perso.move(0,3)
			fenetre.blit(self.direction, self.position_perso)

	def setPosition(self, positionX, positionY):
		 self.position = self.position_perso.move(positionX, positionY)
		 return self.position

	def setPositionInit(self, positionX, positionY):
		 self.position_perso = self.position_perso.move(positionX, positionY)	 