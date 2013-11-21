import sys, os

class ParseSeed:
	def __init__(self, filename, tempdir):
		self.seedfile = filename
		self.tempdir = tempdir
		self.gen_seed_seqs()
	
	def gen_seed_seqs(self): 
		try:
			f = open(self.seedfile)
		except IOError:
			print("File does not exist: %s" % self.seedfile)
			sys.exit(0)
		self.seeds = {}
		for line in f:
			line=line.strip()
			name, seed = line.split()
			self.seeds[name] = seed
	
	def create_in_file(self):
		#Assumes tempdir exits
	
	def get_seeds(self):
		return self.seeds.values()

	def get_seed_ids(self):
		return self.seeds.keys()

		
