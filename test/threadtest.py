from threading import *
from time import *

def test():
    sleep(5)
    print("im a thread")

t = Thread(target=test)
t.start()

print("running loop")

while(True):
    dummy=""
