import os
import time
import random
import fileHandle

lines = fileHandle.getLines("e:/persistence.txt")
random.shuffle(lines)
fname = os.environ.get('TEMP')+"\\test.txt"

#os.system("youtube-dl -g "+lines[0]+" > "+fname)

fileHandle.shuffleLines(lines,fname)
while True:
    #-I dummy --dummy-quiet -vvv
    os.system("vlc -I dummy --dummy-quiet -vvv "+fname+" :sout=#http{dst=192.168.0.169,port=8080,mux=ts,ttl=1} :sout-all :sout-keep vlc://exit")
    time.sleep(1/1000)