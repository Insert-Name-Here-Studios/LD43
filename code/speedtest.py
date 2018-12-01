import pygame
pygame.init()

done = 0

screen = pygame.display.set_mode((800, 800))
x = 25
y = 25

while not done:
	pressed_keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = 1

	if pressed_keys[pygame.K_RIGHT]:
		x += 5
	if pressed_keys[pygame.K_LEFT]:
		x -= 5
	if pressed_keys[pygame.K_UP]:
		y -= 5
	if pressed_keys[pygame.K_DOWN]:
		y += 5

	screen.fill((255, 255, 255))
	pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(x, y, 25, 25))
	pygame.display.flip()

pygame.quit()
quit()
