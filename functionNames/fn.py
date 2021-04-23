import sys

sys.path.append("..\\functions\\")

from fileHandle import *
from os import chdir

def showFunctions(fn,txt):
    
    lines = getLines(fn)

    for line in lines:
        if "def " in line:
            if "(" in line:
                print(txt+line)
        
        elif "function " in line:
            if "(" in line:
                print(txt+line)

        elif "function!" in line:
            print(txt+line)

        
        elif "(" in line:
            if "{" in line:
                if "while" not in line:
                    if "for" not in line:
                        if "if" not in line:
                            print(txt+line)
    
