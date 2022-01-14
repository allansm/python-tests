import sys
sys.path.append("../../python-lib")

from allansm.timeHandle import *
import time
from os import system
from os import chdir

chdir("\\")

shut = int(input("time in hour:"))

t = getTime().split(":")
t[0] = int(t[0])+shut
if(t[0] >= 24):
    t[0]-=24
t[0] = str(t[0])
t = t[0]+":"+t[1]+":"+t[2]

shut = shut*60*60
print("current:"+getTime())
print("shutdown:"+t)
time.sleep(shut)

print(getTime())
system("shutdown /s /f")
