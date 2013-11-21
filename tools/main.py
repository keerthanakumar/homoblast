import sys
from parserconfig import ParseConfig
from parserseed import ParseSeed
from blastsequence import BlastSequence

config = ParseConfig(sys.argv[1])
tempdir = config.get_homoblast_settings()['temp_dir']
seedseq = config.get_homoblast_settings()['seed_seq']
seeds = ParseSeed(seedseq, tempdir)
names = seeds.get_seed_ids()
blast = BlastSequence(tempdir)
#for name in names:
blast.psiblast(names[0])

