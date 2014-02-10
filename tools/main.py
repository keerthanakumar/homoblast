import sys
from parser import ParseConfig, ParseSeed
from jobs import PsiBlast, RunPasta, CombineBlast

config = ParseConfig(sys.argv[1])
tempdir = config.get_homoblast_settings()['temp_dir']
seedseq = config.get_homoblast_settings()['seed_seq']
seeds = ParseSeed(seedseq, tempdir)
names = seeds.get_seed_ids()
for seed in seeds.get_seed_ids():
	runblast = PsiBlast(config, seed)
	runblast.psiblast()
combine = CombineBlast(config, names)
combine.makefastafile()
#RunPasta(config)
