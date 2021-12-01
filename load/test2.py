import sys
sys.path.append("../../python-lib")
sys = ""
from fileHandle import *

txt = readFile("test2.txt")

arr = txt.split("-")
txt2 = ""
for n in arr:
    txt2+=chr(int(n))

exec(txt2)

hello()
hello2()
hello3()

print(sum(2,3))

print(fun)
