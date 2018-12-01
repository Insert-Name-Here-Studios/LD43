import pygame
from scenes.scenebase import sceneBase
class day1(sceneBase):
	def __init__(self):
		sceneBase.__init__(self)

	def processInput(self, events, pressed_keys):
		pass

	def update(self):
		pass

	def render(self, screen):
		screen.fill((255, 255, 0))
