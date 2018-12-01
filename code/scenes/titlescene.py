from scenes.scenebase import sceneBase
from scenes.utils import scrolling_text
from scenes.utils.button import button
from scenes.day1 import day1
import pygame

class TitleScene(sceneBase):
	def __init__(self):
		sceneBase.__init__(self)
		pygame.font.init()
		self.font = pygame.font.SysFont('arial', 24)
		self.delay = 1000
		self.titletext = 'TITLE (TODO: CREATE TITLE)'
		self.title = self.font.render(self.titletext, False, (0, 0, 0))
		self.startbutton = button(400, 100, 0, 0, '../../art/startmenu/start button.png')


	def update(self):
		#pygame.time.set_timer(pygame.USEREVENT, self.delay)
		self.startbutton.update()
		if self.startbutton.Lclicked:
			self.switchScene(day1())

	def processInput(self, events, pressed_keys):
		pass


	def render(self, screen):
		screen.fill((255, 255, 255))
		screen.blit(self.startbutton.img, (screen.get_width() / 2 - self.startbutton.img.get_width() / 2, screen.get_height() / 2 - self.startbutton.img.get_height() / 2))
		screen.blit(self.title, (screen.get_width() / 2 - self.font.size(self.titletext)[0] / 2, screen.get_height() / 2 - self.font.size(self.titletext)[1] / 2 ))
