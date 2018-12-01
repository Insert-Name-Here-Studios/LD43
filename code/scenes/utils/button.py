import pygame

class button(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y, path='', color=None):
		pygame.sprite.Sprite.__init__(self)
		if len(path) > 0:
			self.img = pygame.image.load(path)

		else:
			self.img = pygame.Surface([width, height])
			self.img.fill(color)
		pygame.transform.scale(self.img, (width, height))

		self.Lclicked = False
		self.Rclicked = False

		self.mouseIn = False

		self.rect = pygame.Rect(x, y, self.img.get_width(), self.img.get_height())
		#print(self.rect)

	def update(self):
		mouse_pos = pygame.Rect((pygame.mouse.get_pos()), (1, 1))
		#print(self.rect.x)
		if self.rect.colliderect(mouse_pos):
			#print('YOIT!')
			pygame.event.get()
			if pygame.mouse.get_pressed()[0]:
				self.Lclicked = True
				#print('left clikced!')
			else:
				self.Lclicked = False





			if pygame.mouse.get_pressed()[2]:
				self.Rclicked = True
			else:
				self.Rclicked = False
