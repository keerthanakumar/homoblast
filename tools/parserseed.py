import sys, os

class ParseSeed:
	def __init__(self, filename, tempdir):
		self.seedfile = filename
		self.tempdir = tempdir
		self.gen_seed_seqs()
		self.create_in_files()		

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
	
	def create_in_files(self):
		suffix = '.in'
		seeds = self.seeds
		if not os.path.exists(self.tempdir):
			os.makedirs(self.tempdir)
		for name in self.get_seed_ids():
			fullpath = os.path.join(self.tempdir, name + suffix) 
			print("File Creating %s" % fullpath)
			f = open(fullpath, "w")
			f.write(seeds[name])
			f.close()		
	
	def get_seeds(self):
		return self.seeds.values()

	def get_seed_ids(self):
		return self.seeds.keys()

		
