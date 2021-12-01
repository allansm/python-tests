import sys
sys.path.append("../../python-lib")
sys = ""
from fileHandle import *

txt = readFile("test.txt")
remove("test2.txt")
flag = False
for n in txt:
    if(not flag):
        flag = True
    else:
        writeFile("test2.txt","-")

    writeFile("test2.txt",str(ord(n)))
