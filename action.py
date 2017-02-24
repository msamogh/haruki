class Action(object):

	def __init__(self, driver, fn, xpath=None, data=None, **kwargs):
		self.fn = fn
		self.driver = driver
		self.xpath = xpath
		self.data = data
		self.kwargs = kwargs

	def __call__(self):
		args = [arg for arg in [self.xpath, self.data] if arg]
		if self.xpath:
			element = self.driver.find_element_by_xpath(self.xpath)
			if self.data:
				self.fn(self.driver, element, self.data)
			else:
				self.fn(self.driver, element)
		else:
			self.fn(self.driver, *args, **self.kwargs)


def navigate(driver, **kwargs):
	driver.get(kwargs['url'])

def fill_text_field(driver, input_field, data):
	input_field.send_keys(data)

def click(driver, element):
	element.click()

from selenium.webdriver.support.ui import Select
def select_option(driver, element, option_value):
	select = Select(element)
	select.select_by_value(option_value)

import time
def wait(driver, seconds):
	time.sleep(seconds)