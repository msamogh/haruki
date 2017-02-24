from lxml import etree

class Scraper:
	"""All scrapers must extend Scraper"""

	# Constants
	TEXT = 'string()' # XPath property for text inside tag

	memo = {}

	def __init__(self, name, driver, memoize=False):
		self.name = name
		self.driver = driver
		self.memoize = memoize

	@staticmethod
	def xpath(root=None, attr=None, **paths):
		"""Calls the original function with the located nodes at the given paths as argument"""
		def wrap(f):
			def wrapped_f(*args):
				self = args[0]

				# Prepend root to all paths if root is not None
				if root:
					for path in paths:
						paths[path] = root + paths[path]				

				# Check if args already memoized
				if self.memoize:
					if hash(tuple(sorted(paths.items()))) in Scraper.memo:
						return dict((x, y) for x, y in memo[hash(tuple(sorted(paths.items())))])

				# Retrieve nodes at paths
				html = etree.HTML(self.driver.page_source)
				target_nodes = {path: html.find(paths[path]) for path in paths}

				if attr:
					for node in target_nodes:
						target_nodes[node] = target_nodes[node].xpath(attr)

				# Update memo
				if self.memoize:
					Scraper.memo[hash(tuple(sorted(paths.items())))] = target_nodes

				# Call original function with updated args
				updated_args = [self, target_nodes]
				return f(*updated_args)
			return wrapped_f
		return wrap
