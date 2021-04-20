import sys

sys.path.append("../functions")

from fileHandle import *

from os import chdir

import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument("code",type=str)
parser.add_argument("path",type=str)

code = parser.parse_args().code

chdir(parser.parse_args().path)

lines = getLines(code)

print(code+":")

for line in lines:
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
     
