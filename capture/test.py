import sys
sys.path.append("../../python-lib")

from imageHandle import *
from fileHandle import *
from elapse import *
from os import chdir,mkdir,getcwd

chdir(getTemp())
try:
    mkdir("capturetest")
except:
    dummy=""

chdir("capturetest")
print(getcwd())
i=0
while(True):
    e = Elapse()
    fn = '{:0>3}'.format(i)
    ss = screenshot()
    ss.save(fn+".jpg",quality=1)
    i+=1
    print(e.elapsed())

