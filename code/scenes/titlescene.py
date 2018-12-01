from scenes.scenebase import sceneBase
from scenes.utils import scrolling_text
import pygame

class TitleScene(sceneBase):
	def __init__(self):
		sceneBase.__init__(self)
		pygame.font.init()
		self.font = pygame.font.SysFont('arial', 24)
		self.delay = 1000
		self.titletext = 'TITLE (TODO: CREATE TITLE)'
		self.title = self.font.render(self.titletext, False, (0, 0, 0))


	def update(self):
		#pygame.time.set_timer(pygame.USEREVENT, self.delay)
		pass

	def processInput(self, events, pressed_keys):
		pass


	def render(self, screen):
		screen.fill((255, 255, 255))
		screen.blit(self.title, (screen.get_width() / 2 - self.font.size(self.titletext)[0] / 2, screen.get_height() / 2 - self.font.size(self.titletext)[1] / 2 ))
