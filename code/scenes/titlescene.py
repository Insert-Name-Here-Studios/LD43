from scenebase import sceneBase
from utils import scrolling_text
import pygame

class TitleScene(sceneBase):
	def __init__(self):
		sceneBase.__init__(self)
		self.font = pygame.font.SysFont('arial', 24)
		self.delay = 1000
		pygame.time.set_timer(pygame.USEREVENT, 200)
		self.textbox = scrolling_text.DynamicText(self.font, ['test sentence for ^the boys', 'Yeeeeeeee^eeeeeeet'], (500, 200), (0, 0, 0))

	def update(self):
		#pygame.time.set_timer(pygame.USEREVENT, self.delay)
		pass

	def processInput(self, events, pressed_keys):
		for event in events:
			if event.type == pygame.USEREVENT:
				self.textbox.update()



	def render(self, screen):
		screen.fill((255, 255, 255))
		self.textbox.draw(screen)
