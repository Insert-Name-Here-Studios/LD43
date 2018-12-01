from scenes.scenebase import sceneBase
from scenes.utils.scrolling_text import DynamicText
from scenes.utils.button import button
from scenes.utils.textbox import TextBox
from scenes.day1 import day1
import pygame
import os

class TitleScene(sceneBase):
	def __init__(self):
		sceneBase.__init__(self)
		pygame.font.init()
		self.font = pygame.font.Font('fonts/retro.TTF', 48)

		self.delay = 1000
		self.titletext = 'The Innocent'
		self.title = self.font.render(self.titletext, False, (0, 0, 0))
		self.startbutton = button(400, 100, 0, 0, 'art/button.png')

		#self.tb = TextBox(DynamicText(self.font, ['YEEET', 'No uuuuuuuu'], (55, 76), (255, 0, 255)), 'art\dtb.png', 5, 500, 100)


	def update(self):
		#pygame.time.set_timer(pygame.USEREVENT, self.delay)
		self.startbutton.update()
		if self.startbutton.Lclicked:
			self.switchScene(day1())
		self.tb.update()



	def processInput(self, events, pressed_keys):
		pass


	def render(self, screen):
		screen.fill((255, 255, 255))
		screen.blit(self.startbutton.img, (screen.get_width() / 2 - self.startbutton.img.get_width() / 2, screen.get_height() / 2 - self.startbutton.img.get_height() / 2))
		self.startbutton.pos = (screen.get_width() / 2 - self.startbutton.img.get_width() / 2, screen.get_height() / 2 - self.startbutton.img.get_height() / 2)
		screen.blit(self.title, (screen.get_width() / 2 - self.font.size(self.titletext)[0] / 2, screen.get_height() / 2 - self.font.size(self.titletext)[1] / 2 - 200 ))
		self.tb.render(screen)
