import sys

sys.path.append("../functions")

from fileHandle import *
from argsHandle import *
from os import chdir

try:
    args = getArgs(["text","op","backup"],"")
    
    text = args.text
    op = args.op
    backup = args.backup

    chdir(getTemp())

    chdir("search")
    if(backup == None):
        found = getLines(".found")
    else:
        print("using:"+backup)
        found = getLines(backup)

    if(op == "file"):
        for registry in found:
            fn = getFileName(registry)
            if(text.lower() in fn.lower()):
                    print(registry)
 
    else:
        for registry in found:
            if(text.lower() in registry.lower()):
                if(op == "filename"):
                    fn = getFileName(registry)
                    if(fn != ""):
                        print(fn)
                else:
                    print(registry)
except:
    print("has no path stored.")


