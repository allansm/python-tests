#import sys
#sys.path.append("../functions")
#from dependency import *

def dependency():
    import argsHandle
    import timeHandle
    import fileHandle
    import util

    global getArgs
    getArgs = argsHandle.getArgs

    global getDate
    global getTime
    getDate = timeHandle.getDate
    getTime = timeHandle.getTime

    global ls
    global selfLocation
    ls = fileHandle.ls
    selfLocation = fileHandle.selfLocation

    global print_r
    print_r = util.showOptions

def test():    
    include("../functions",dependency,"../test")

    print(getDate())
    print(getTime())

    print_r(ls(".","*"))

    print(selfLocation(__file__))

#wrong
def test2():
    import os

    tmp = os.getcwd()
    
    from os.path import dirname,realpath
    os.chdir(dirname(realpath(__file__)))
    os.chdir("../functions")

    from timeHandle import getTime
    global getTime

    os.chdir(tmp)

def test3(path):
    import sys
    import os
    from os.path import dirname,realpath
    from glob import glob
    
    tmp = os.getcwd()
    os.chdir(dirname(realpath(__file__)))

    anyFile = glob(path+"/*")[0]
    path = dirname(realpath(anyFile))

    sys.path.append(path)

    os.chdir(tmp)

test3("../functions")
import os

os.chdir("c:\\")

from timeHandle import *
print(getTime())

