import os
import time
import random
import fileHandle
import threading

def thread_function(name):
    lines = fileHandle.getLines("e:/persistence.txt")
    fname = os.environ.get('TEMP')+"\\test.txt"
    while True:
        random.shuffle(lines)
        start = time.time()
        os.system("echo im running..")
        os.system("youtube-dl --get-url --format best "+lines[0]+" > "+fname)
        end = time.time()
        os.system("echo "+str(end-start))
        os.system("echo im sleeping..")
        time.sleep(600*3)
    
x = threading.Thread(target=thread_function, args=(1,))
x.start()

fname = os.environ.get('TEMP')+"\\test.txt"

while True:
    os.system("vlc "+fname+" vlc://quit")
    time.sleep(1/1000)