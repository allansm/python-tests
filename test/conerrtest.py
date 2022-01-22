import sys
sys.path.append("../../python-lib")
from allansm.socketHandle import *
import errno
import socket
import os

arr = []
for n in range(180,253):
    try:
        client("192.168.0."+str(n),80,print,timeout=3)
    except socket.error as error:
        if error.errno == errno.ECONNREFUSED:
            arr.append(n)
            print("ok:"+str(n))
        else:
            print("ignored:"+str(n))
print(arr)
