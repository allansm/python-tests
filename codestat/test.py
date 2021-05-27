import sys

sys.path.append("../functions")

from fileHandle import *

import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--folder",required=False)
    args = parser.parse_args()
    
    return args

def countLines(fname):
    return len(getLines(fname))-1


args = getArgs()

folder = args.folder

files = getAllFiles(folder)

extension = [".py",".php",".java",".cpp",".html"]
name = ["python","php","java","c++","html"]
count = [0,0,0,0,0]

for f in files:
    for e in extension:
        try:
            if(e in f):
                count[extension.index(e)] = count[extension.index(e)] +  countLines(f)
                #print("file:"+f+" lines:"+str(countLines(f)))
        except:
            dummy = ""
            #print("error")
for n in name:
    print(n+":"+str(count[name.index(n)])+" lines")
