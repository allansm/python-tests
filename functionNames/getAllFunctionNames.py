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


functions = ""

for f in fold:
    if(os.path.isfile(f)):
        fun = getFunctions(f,"",";")
        if(fun != "" or not fun):
            functions = functions+";"+fun
    else:
        chdir(f)

        files = ls(".","*.*")

        for fi in files:
            try:
                fun = getFunctions(fi,"",";")
                if(fun != "" or not fun):
                    functions = functions+";"+fun
            except:
                continue
        
        chdir("..")

functions = functions.replace(";","")
functions = removeBreakLine(functions)
functions = functions.replace("{","?@?")
functions = functions.replace(":","?@?")
print(functions)
