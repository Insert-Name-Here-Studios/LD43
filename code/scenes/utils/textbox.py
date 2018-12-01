import pygame

# tb = TextBox(DynamicText(self.tb_font, 'YEEET', (55, 76), (255, 0, 255)), '../../art/day2/tb.png', 500)


class TextBox:
    def __init__(self, dynatext, path, delay, w, h):
		self.textbox_x = dynatext.pos[0] - 10
		self.textbox_y = dynatext.pos[1] - 5

		try:
		    self.img = pygame.image.load(path)
		except:
			print('error loading image')

		self.img = pygame.transform.scale(self.img, (w, h))
		self.dynatext = dynatext

		self.rect = pygame.Rect(self.textbox_x, self.textbox_y, self.img.get_width(), self.img.get_height())

		pygame.time.set_timer(pygame.USEREVENT, delay)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.dynatext.update()


    def render(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        self.dynatext.draw(screen)
