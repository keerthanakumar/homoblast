import ConfigParser
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
