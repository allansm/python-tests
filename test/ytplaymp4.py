import sys

sys.path.append("../functions")

from fileHandle import *
from subprocess import call
from os import chdir
from os import mkdir
from util import *

chdir(getTemp())

try:
    mkdir("ytplaymp4")    
except:
    print("...")

chdir("ytplaymp4")

txt = input("links file url:")

lines = getLines(txt)

shuffled = fakeshuffle(lines)

writeLines("persistence.txt",shuffled)

newlines = getLines("persistence.txt")

for line in newlines:
    call("youtube-dl --get-url --format best "+line+" > current",shell=True)
    call("ffplay -an -noborder -x 300 -y 200 -top 0 -left 0 "+getLines("current")[0])


