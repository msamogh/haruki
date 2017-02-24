class Action(object):

	def __init__(self, fn, driver, **kwargs):
		self.fn = fn
		self.driver = driver
		self.kwargs = kwargs

	def __call__(self):
		self.fn(self.driver, **self.kwargs)

	@staticmethod
	def navigate(driver, **kwargs):
		driver.get(kwargs['url'])



class XPathAction(Action):

	def __init__(self, fn, driver, xpath):
		self.