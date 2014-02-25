import os, subprocess
from Bio import Entrez, SeqIO
from parser import ParseConfig


class PsiBlast:
	
	def __init__(self, config, seq ): #Should ideally make it **kwargs
	#	Job.__init__(self)
		self.job_type="psi_blast"
		self.tempdir = config.get_homoblast_settings()['temp_dir']
		self.seq = seq
		self.settings = config.get_psiblast_settings()
		#Create a stdout and stdin here
	
	def psiblast(self):
		insuf = '.in'
		infile = os.path.join(self.tempdir, self.seq + insuf)
		#infile = '-query ' + infile
		outsuf = '.out'
		outfile = os.path.join(self.tempdir, self.seq + outsuf)
		#outfile = '-out ' + outfile
		# Figuring out how subprocessors work
		# Need to set up jobs and multithread
		subprocess.call([self.settings['executable'], "-db","nr","-out", outfile, "-query", infile, "-num_iterations", self.settings['num_iterations'], "-evalue", self.settings['e_value'], "-outfmt", self.settings['outfmt']])

class CombineBlast:
	def __init__(self, config, seednames):
		self.job_type = "combine_blast"
		self.tempdir = config.get_homoblast_settings()['temp_dir']
		self.returndir = config.get_homoblast_settings()['return_dir']
		self.settings = config.get_entrez_settings()
		self.fastafilename = self.settings['fasta_file_name']
		self.email = self.settings['email']
		self.fastafile = os.path.join(self.returndir, self.fastafilename+".fasta")
		self.outfiles = []
		for seed in seednames:
			self.outfiles.append(os.path.join(self.tempdir, seed+".out"))
		self.accs = set()
		self.makeaccsset()
	
	def makeaccsset(self):
		for out in self.outfiles:
			f = open(out, "r")
			for line in f:
				line = line.strip()
				if "gi" in line:
					acc = line.split()[1].split("|")[3]
				if len(acc) > 5:
					self.accs.add(acc)
			f.close()

	def makefastafile(self):
		fastatext = ""
		Entrez.email = self.email
		for acc in self.accs:
			fetch = Entrez.efetch(db="protein", rettype="gb", retmode="text", id=acc)
			io = SeqIO.read(fetch, "gb")
			fasta = "> "+io.id+" " +io.annotations["taxonomy"][0]+"\n"
			fasta += str(io.seq)+"\n"
			fastatext += fasta
		f = open(self.fastafile, "w")
		f.write(fastatext)
		f.close()		

	def getFasta(self):
		return self.fastafile

class RunPasta:
	def __init__(self, config):
		self.job_type = "run_pasta"
		self.configfile = config.get_pasta_settings()['pasta_config_file']
		self.run_pasta()

	def run_pasta(self):
		 subprocess.call(["python", "/home/kk24268/blast/pasta-master", self.configfile])
