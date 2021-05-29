import sys

sys.path.append("../functions")

from fileHandle import *

import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--folders",required=False)
    parser.add_argument("--extensions",required=False)
    parser.add_argument("--names",required=False)
 
    args = parser.parse_args()
    
    return args

def countLines(fname):
    return len(getLines(fname))-1


def getTotal(count):
    total = 0

    for c in count:
        total = total + c
    
    return total

def getPercent(count):
    total = getTotal(count)

    percent = []
    for c in count:
        tmp = (c / total) * 100
        tmp = format(tmp,".2f")
        percent.append(tmp)
    
    return percent

def getStats(folders,extensions,names):
    files = []
    for folder in folders:
        files = files + getAllFiles(folder)

    extension = extensions.split(";")
    count = []
    n = []
    for e in extension:
        count.append(0)
        n.append(0)

    name = names.split(";")

    for f in files:
        for e in extension:
            try:
                if(e in f):
                    count[extension.index(e)] = count[extension.index(e)] +  countLines(f)
                    n[extension.index(e)] = n[extension.index(e)] + 1
 
            except:
                dummy = ""
    
    percent = getPercent(count)

    stats = []
    stats.append(extension)
    stats.append(name)
    stats.append(count)
    stats.append(percent)
    stats.append(n)

    return stats

def console():
    args = getArgs()

    txt = args.folders
    names = args.names
    extensions = args.extensions

    folders = getLines(txt)

    stats = getStats(folders,extensions,names)

    name = stats[1]
    count = stats[2]
    percent = stats[3]
    files = stats[4]

    for n in name:
        print(n+": lines percent "+str(percent[name.index(n)])+"% "+str(count[name.index(n)])+" lines "+str(files[name.index(n)])+" files")

    print("\ntotal lines:"+str(getTotal(count)))

console()
