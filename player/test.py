from dependency import *

include("../../python-lib")

from ff import playSound as ffplay
from fileHandle import getAllFilesPath as files
from fileHandle import getLines,isdir
from argsHandle import *
from random import shuffle
from util import toast

args = getArgs(["files"])

'''
if(not isdir(args.files)):
    arr = []
    for line in getLines(args.files):
'''
files = files(args.files)

shuffle(files)

for n in files:
    toast(n,"listening:")
    print("listening:"+n)
    ffplay(n)
