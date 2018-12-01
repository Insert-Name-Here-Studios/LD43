import scenebase
sb = scenebase.sceneBase()
class TitleScene(sb):
	def __init__(self):
		sb.__init__(self)

	def update(self):
		pass

	def processInput(self, events, pressed_keys):
		pass

	def render(self, screen):
		screen.fill((0, 0, 0))
