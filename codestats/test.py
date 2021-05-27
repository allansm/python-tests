#note add files count and lines count to output

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


def getStats(folders,extensions,names):
    files = []
    for folder in folders:
        files = files + getAllFiles(folder)

    #extension = [".py",".php",".java",".cpp",".html",".asm",".txt",".bat"]
    extension = extensions.split(";")
    count = []
    for e in extension:
        count.append(0)

    #name = ["python","php","java","c++","html","assembly","text","windows shell"]
    name = names.split(";")
    #count = [0,0,0,0,0,0,0,0]

    for f in files:
        for e in extension:
            try:
                if(e in f):
                    count[extension.index(e)] = count[extension.index(e)] +  countLines(f)
                    
            except:
                dummy = ""
    
    stats = []
    stats.append(extension)
    stats.append(name)
    stats.append(count)
    
    return stats

def test(count):
    total = 0

    for c in count:
        total = total + c
    
    percent = []
    for c in count:
        tmp = (c / total) * 100
        #tmp = round(tmp)
        tmp = format(tmp,".2f")
        percent.append(tmp)
    
    return percent

args = getArgs()

txt = args.folders
names = args.names
extensions = args.extensions

folders = getLines(txt)

stats = getStats(folders,extensions,names)

name = stats[1]
count = stats[2]

'''
total = 0

for c in count:
    total = total + c
'''

percent = test(count)
for n in name:
    print(n+":"+str(percent[name.index(n)])+"%") #str(count[name.index(n)])+" lines")

