def runGame(width, height, fps, startingScene, title='DEFAULT TITLE'):
	pygame.init()
	screenDims = (width, height)
	screen = pygame.display.set_mode(screenDims, pygame.RESIZABLE)
	pygame.display.set_caption(title)
	clock = pygame.time.Clock()

	activeScene = startingScene

	while activeScene != None:
		pressed_keys = pygame.key.get_pressed()

		filteredEvents = []
		for event in pygame.event.get():
			quit_attempt = False
			if event.type == pygame.QUIT:
				quit_attempt = True
			elif event.type == pygame.KEYDOWN:
				alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
				if event.key == pygame.K_F4 and alt_pressed:
					quit_attempt = True
			elif event.type == pygame.VIDEORESIZE:


			if quit_attempt:
				activeScene.terminate()
			else:
				filteredEvents.append(event)

		activeScene.processInput(filteredEvents, pressed_keys)
		activeScene.update()
		activeScene.render(screen)

		activeScene = activeScene.next

		pygame.display.flip()
		clock.tick(fps)
