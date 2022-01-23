import sys
sys.path.append("../../python-lib")
from allansm.socketHandle import *
import errno
import socket
import os
from threading import *
from allansm.elapse import *

def verify(a,n):
    global arr,i

    for n in range(a,n):
        try:
            client("192.168.0."+str(n),80,print,timeout=3)
        except socket.error as error:
            if error.errno == errno.ECONNREFUSED:
                arr.append(n)
                #print("ok:"+str(n))
            #else:
               #print("ignored:"+str(n))
    i+=1

elapse = Elapse()

arr = []
i = 1
last = 2
for n in range(1,85):
    Thread(target=lambda : verify(last,3*n)).start()
    last=3*n

print(last)
Thread(target=lambda : verify(last,253)).start()

while(i < 20):
    dummy=0

print(arr)
print(elapse.elapsed())
input()
