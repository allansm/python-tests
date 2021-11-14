import sys
sys.path.append("../../python-lib")

import socketHandle as sh
from fileHandle import *
from argsHandle import *


fn = getArgs(["fn"]).fn

def send(s):
    data = s.recv(1024)
    f= open(fn,"rb")
    tosend = f.read()
    #tosend = readFile(fn)
    s.sendall(tosend)


sh.server(54321,send)
