import test3
import sys
sys.path.append("../../python-lib")

from util import exec

def action(s):
    data = s.recv(1024)
 
    s.sendall(test3.http("hello world").encode("utf-8"))

#while True:
#    test3.server(9090,action)

def action2(s):
    s.sendall("dir".encode("utf-8"))
    data = s.recv(1024)

test3.client('127.0.0.1',65432,action2)
