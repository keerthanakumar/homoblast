import sys
from parserconfig import ParserConfig

config = ParserConfig(sys.argv[1])
print config.get_homoblast_settings()
#print config
