import pygame

def text_generator(texts):
	for text in texts:
		tmp = ''
		for letter in text:
			tmp += letter
			# don't pause for spaces
			if letter != ' ':
				yield tmp
# a simple class that uses the generator
# and can tell if it is done
class DynamicText(object):
    def __init__(self, font, text, pos, color=(0, 0, 0), autoreset=False):
		self.done = False
		self.font = font
		self.text = text
		self._gen = text_generator(self.text)
		self.pos = pos
		self.color = color
		self.autoreset = autoreset
		self.update()



    def reset(self):
		self._gen = text_generator(self.text)
		self.done = False
		self.update()

    def update(self):

        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, self.color)
            except StopIteration:
                self.done = True
                if self.autoreset: self.reset()

    def draw(self, screen):
		
		screen.blit(self.rendered, self.pos)
