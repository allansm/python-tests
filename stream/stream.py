'''import os
import time
import random
import fileHandle

lines = fileHandle.getLines("e:/persistence.txt")
fname = os.environ.get('TEMP')+"\\test.txt"

while True:
    random.shuffle(lines)
    os.system("youtube-dl --get-url --format best "+lines[0]+" | vlc -I dummy --dummy-quiet - :sout=#http{dst=192.168.0.169,port=8080,mux=ts,ttl=1} :sout-all :sout-keep vlc://quit")
    time.sleep(1/1000)'''