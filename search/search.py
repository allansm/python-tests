#import sys

#sys.path.append("../functions")
import dependency

from fileHandle import *
from argsHandle import *
from os import chdir

try:
    args = getArgs(["--text","--op","--backup","--ext"])
    
    text = args.text
    op = args.op
    backup = args.backup
    ext = args.ext

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
                if(ext != None):
                    if(ext in registry):
                        print(registry)
                else:
                    print(registry)
    else:
        for registry in found:
            if(text.lower() in registry.lower()):
                if(op == "filename"):
                    fn = getFileName(registry)
                    if(fn != ""):
                        if(ext != None):
                            if(ext in registry):
                                print(fn)
                        else:
                            print(fn)

                else:
                    if(ext != None):
                        if(ext in registry):
                            print(registry)
                    else:
                        print(registry)

except:
    print("has no path stored.")


