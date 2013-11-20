import ConfigParser

class ParserConfig:
	def __init__(self, filename=None):
		self.configfile = filename
		self.config = ConfigParser.ConfigParser()	
		self.config.read(self.configfile)
		self.homoblast_settings()

	def homoblast_settings(self):
		homoblast='HOMO-BLAST'
		options = ['seed_seq', 'working_dir', 'general']
		self.hb_opt = {}
		for option in options:
			try:
				self.hb_opt[option] = self.config.get(homoblast, option)
			except:
				self.hb_opt[option] = None		
	
	def get_homoblast_settings(self):
		return self.hb_opt
