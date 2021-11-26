import sys
sys.path.append("../../python-lib")

from imageHandle import *
from fileHandle import *
from elapse import *
from os import chdir,mkdir,getcwd

chdir(getTemp())

remove("capturetest")
mkdir("capturetest")
chdir("capturetest")

print(getcwd())

i=0
count = 0
e = Elapse()
while(True):
    if(e.elapsed() > 60000):
        print(count/60)
        count = 0
        e = Elapse()

    fn = str(i)#'{:0>3}'.format(i)
    ss = screenshot()
    ss.save(fn+".jpg",quality=33)
    i+=1
    count+=1

