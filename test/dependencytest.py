def include(path,dependency):
    import os
    import sys
    from os.path import dirname,realpath

    tmp = os.getcwd()
    os.chdir(dirname(realpath(__file__)))
    sys.path.append(path)
    dependency()
    os.chdir(tmp)

def tmp():
    import argsHandle
    
    global getArgs
    getArgs = argsHandle.getArgs
    
include("../functions",tmp)

works = getArgs(["works"]).works

print(works)
