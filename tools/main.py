import sys
from parserconfig import ParseConfig
from parserseed import ParseSeed

config = ParseConfig(sys.argv[1])
#print config.get_homoblast_settings()['temp_dir']
seeds = ParseSeed(config.get_homoblast_settings()['seed_seq'],config.get_homoblast_settings()['temp_dir'])
print seeds.get_seed_ids()
