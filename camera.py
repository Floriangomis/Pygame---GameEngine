import pygame
from pygame.locals import *

WIN_WIDTH = 800
WIN_HEIGHT = 600
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)


class Camera(object):
	def __init__(self, width, height):
		self.state = Rect(0, 0, width, height)

	def simple_camera(self, camera, target_rect):
		l, t, _, _ = target_rect 	# l = left,  t = top
		_, _, w, h = camera			# w = width, h = height
		return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

	def apply(self, target):
		return target.move(self.state.topleft)
	
	def update(self, target):
		self.state = self.simple_camera(self.state, target.rectPerso)