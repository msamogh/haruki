class Robot(object):

	def __init__(self, name, actions, scraper):
		self.name = name
		self.actions = actions
		self.scraper = scraper

	def run(self):
		for a in self.actions:
			a()

 