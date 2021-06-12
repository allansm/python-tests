import sys

sys.path.append("../functions")

from fileHandle import *
from argsHandle import *
from os import chdir

try:
    args = getArgs(["text","op"],"")
    
    text = args.text
    op = args.op

    chdir(getTemp())

    chdir("search")
    found = getLines(".found")

    for registry in found:
        if(text in registry):
            if(op == "filename"):
                fn = getFileName(registry)
                if(fn != ""):
                    print(fn)
            else:
                print(registry)
except:
    print("has no path stored.")


