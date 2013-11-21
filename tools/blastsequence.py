import os, subprocess

class BlastSequence:
	
	def __init__(self, tempdir):
		self.tempdir = tempdir
	
	def psiblast(self, seq):
		insuf = '.in'
		infile = os.path.join(self.tempdir, seq	+ insuf)
		infile = '-query ' + infile
		outsuf = '.out'
		outfile = os.path.join(self.tempdir, seq + outsuf)
		outfile = '-out ' + outfile
		# Figuring out how subprocessors work
		# Need to set up jobs and multithread 
#		subprocess.check_output(["psiblast", '-db nr', outfile, infile, "-num_iterations 3", "-e value 1", "-outfmt 6"], shell=True)	
