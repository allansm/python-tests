from allansm.elapse import *
from allansm.imageHandle import *
from threading import *
from time import sleep

count = 0

def test():
    global count

    screenshot()
    count+=1
    
e = Elapse()
for n in range(0,30):
    tmp = Thread(target=test)
    tmp.start()

print("waiting..")
while(count < 30):
    dummy=0

print(e.elapsed())
print(count)
