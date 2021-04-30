import sys
import os

wdir = os.path.dirname(os.path.realpath(__file__))


sys.path.append(wdir)
sys.path.append(wdir+"/../functions")

from fileHandle import *

from os import chdir
from os import getcwd
from fn import *

import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument("code",type=str)

code = parser.parse_args().code

chdir(getcwd())

if(os.path.isfile(code)):

    print(code+":")
    showFunctions(code,"    ")

else:
    chdir(code)

    files = ls(".","*.*")

    for f in files:
        print(f+":")
        showFunctions(f,"   ")
        print("")
