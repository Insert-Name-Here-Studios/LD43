import pygame
class sceneBase:
	def __init__(self):
		pygame.font.init()
		self.next = self

	def processInput(self, events, pressed_keys):
		print('Not overridden in chile class!')

	def update(self):
		print('Not overridden in chile class!')

	def render(self, screen):
		print('Not overridden in chile class!')

	def switchScene(self, next_scene):
		self.next = next_scene

	def terminate(self):
		self.switchScene(None)
