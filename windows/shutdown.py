import time
from os import system
from os import chdir

chdir("\\")

shut = int(input("time in hour:"))*60*60

print(time.ctime())

time.sleep(shut)

print(time.ctime())

system("shutdown /s /f")
