from scenebase import sceneBase

class TitleScene(sceneBase):
	def __init__(self):
		sceneBase.__init__(self)

	def update(self):
		pass

	def processInput(self, events, pressed_keys):
		pass

	def render(self, screen):
		screen.fill((255, 0, 0))
