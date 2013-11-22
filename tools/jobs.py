import os, subprocess

class Job:
	def __init__(self):
		self.result = None
		self.errors = []
	
	def __call__(self):
		return self.run()
	
	def run(self):
		raise NotImplementedError;


class PSI_BLSAT(Job):
	
	def __init__(self, tempdir, seq ): #Should ideally make it **kwargs
		Job.__init__(self)
		self._id = None
		self.tempdir = tempdir
		self.seq = seq
		#Create a stdout and stdin here
	
	def psiblast(self):
		insuf = '.in'
		infile = os.path.join(self.tempdir, self.seq	+ insuf)
		infile = '-query ' + infile
		outsuf = '.out'
		outfile = os.path.join(self.tempdir, self.seq + outsuf)
		outfile = '-out ' + outfile
		# Figuring out how subprocessors work
		# Need to set up jobs and multithread 
#		subprocess.check_output(["psiblast", '-db nr', outfile, infile, "-num_iterations 3", "-e value 1", "-outfmt 6"], shell=True)	
