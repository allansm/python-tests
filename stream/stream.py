import os
import time
import random
from functions import *

list = readFile("links.txt").split("\n")
'''
while(True):
    random.shuffle(list)
    print(list[0])
    time.sleep(0.5)
'''
random.shuffle(list)

remove("test.txt")

createFile("test.txt")

for n in list:
    writeFile("test.txt",n+"\n")
    
os.system("vlc test.txt")