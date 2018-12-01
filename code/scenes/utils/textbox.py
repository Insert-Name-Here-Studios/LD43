import pygame

# tb = TextBox(DynamicText(self.tb_font, 'YEEET', (55, 76), (255, 0, 255)), '../../art/day2/tb.png', 500)


class TextBox:
    def __init__(self, dynatext, path, delay):
        self.textbox_x = dynatext.pos[0] - 10
        self.textbox_y = dynatext.pos[1] - 5
        self.textbox_w = dynatext.font.size(dynatext.text)[0] + 20
        self.textbox_h = dynatext.font.size(dynatext.text)[1] + 10
        self.dynatext = dynatext
        try:
            self.img = pygame.image.load(path)
        except SyntaxError:
            print('ya dun goofed the syntax')
        finally:
            print('error loading image')

        pygame.transform.scale(self.img, (self.textbox_w, self.textbox_h))

        self.rect = pygame.Rect(self.textbox_x, self.textbox_y, self.img.get_width(), self.img.get_height())

        pygame.time.timer(pygame.USEREVENT, delay)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.dynatext.update()

    def render(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        self.dynatext.draw(screen)
