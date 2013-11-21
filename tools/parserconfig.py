import ConfigParser

class ParseConfig:
	def __init__(self, filename=None):
		self.configfile = filename
		self.config = ConfigParser.ConfigParser()	
		self.config.read(self.configfile)
		self.generate_settings()

	def generate_settings(self):
		homoblast='HOMO-BLAST'
		#TODO:Set up option dictionay with defaults
		hboptions = ['seed_seq', 'temp_dir', 'return_dir',' keeptemp']
		psioptions = ['e_value', 'num_iterations', 'outfmt', 'max_target_seqs']
		self.hb_opt = {}
		self.psi_opt = {}
		for option in hboptions:
			try:
				self.hb_opt[option] = self.config.get(homoblast, option)
			except:	
				#TODO:Need to still set up default settings
				self.hb_opt[option] = None		
		for option in psioptions:
			try:
				self.psi_opt[option] = self.config.get(homoblast, option)
			except:
				#TODO: Need to stil set up default settings
				self.psi_opt[option] = None
	
	def get_homoblast_settings(self):
		return self.hb_opt
	
	def get_psiblast_settings(self):
		return self.psi_opt
