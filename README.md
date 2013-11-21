homoblast
=========
PSI-Blasting Homologies

Author: Keerthana Kumar

Given a file with seed sequences and other specifications you can generate a FASTA file with all unique results of PSI blast. Need NCBI's nr database and ~/.ncbirc pointing to the nr database for proper functionality. Requires at least ncbi-blast-2.2.28+ for psiblast functionality. Requires biopython for generating fasta file.

Look out to understand how this should be run for sample config.txt file.

----Checking my progress------

Competely added to repo:
	1. Parse the config file
	2. Get seed sequences (current tested only for accession number)
	3. Make seed seq-in files in temp directory

At least partial implementation done:
	1. Run PSI-Blast on each seq with particular e-value (found in config file), num_iterations (default = 3)
	2. Parse seq-out files combine accession numbers in <seed seq file>.acc
	3. Generate fasta file from all these accession numbers <seed seq file>.fasta

Still to do:
	> Generate a taxonomical information for all the sequences <seed seq file>_<e-value>.md
	> Mutli-thread the whole process, especially generating fastafiles
	> Alignment tool (Oh no :\ )
	> Tree tool
	> Analysing Tree tool?
