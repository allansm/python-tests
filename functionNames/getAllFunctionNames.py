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



chdir(code)
chdir("..")

fold = ls(".","*")


functions = code+","

for f in fold:
    if(os.path.isfile(f)):
        fun = getFunctions(f,"")
        if(fun != ""):
            functions = functions+","+fun
    else:
        chdir(f)

        files = ls(".","*.*")

        for fi in files:
            try:
                fun = getFunctions(fi,"")
                if(fun != ""):
                    functions = functions+","+fun
            except:
                continue
        
        chdir("..")

print(functions)
