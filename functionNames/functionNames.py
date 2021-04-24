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

#lines = getLines(code)

print(code+":")

showFunctions(code,"    ")

'''for line in lines:
    if "def " in line:
        if "(" in line:
            print("     "+line)
    
    elif "function " in line:
        if "(" in line:
            print("     "+line)

    elif "function!" in line:
        print("     "+line)

    
    elif "(" in line:
        if "{" in line:
            if "while" not in line:
                if "for" not in line:
                    if "if" not in line:
                        print("    "+line)
   '''  
