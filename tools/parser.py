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
		psiblast = 'PSI-BLAST'
		entrez = 'ENTREZ'
		pasta = 'PASTA'
		#TODO:Set up option dictionay with defaults
		hboptions = ['seed_seq', 'temp_dir', 'return_dir',' keeptemp']
		psioptions = ['e_value', 'num_iterations', 'outfmt', 'max_target_seqs']
		entrezoptions = ['email','fasta_file_name']
		pastaoptions = ['pasta_config_file']
		self.hb_opt = {}
		self.psi_opt = {}
		self.entrez_opt = {}
		self.pasta_opt = {}
		for option in hboptions:
			try:
				self.hb_opt[option] = self.config.get(homoblast, option)
			except:	
				#TODO:Need to still set up default settings
				self.hb_opt[option] = None		
		for option in psioptions:
			try:
				self.psi_opt[option] = self.config.get(psiblast, option)
			except:
				#TODO: Need to stil set up default settings
				self.psi_opt[option] = None
		for option in entrezoptions:
			try:
				self.entrez_opt[option] = self.config.get(entrez, option)
			except:	
				#TODO:Need to still set up default settings
				self.entrez_opt[option] = None		
		for option in pastaoptions:
			try:
				self.pasta_opt[option] = self.config.get(pasta, option)
			except:	
				#TODO:Need to still set up default settings
				self.pasta_opt[option] = None		
		
	def get_homoblast_settings(self):
		return self.hb_opt
	
	def get_psiblast_settings(self):
		return self.psi_opt

	def get_entrez_settings(self):
		return self.entrez_opt
	
	def get_pasta_settings(self):
		return self.pasta_opt
