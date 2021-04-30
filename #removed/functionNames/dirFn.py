import sys

sys.path.append("../functions")

from fileHandle import *
from os import chdir
from fn import *

import argparse

parser = argparse.ArgumentParser(description='')

parser.add_argument("path",type=str)

chdir(parser.parse_args().path)

files = ls(".","*.*")

for f in files:
    showFunctions(f,"")
