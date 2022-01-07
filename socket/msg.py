import sys
sys.path.append("../../python-lib")

import socketHandle as sh
from threading import *
from time import sleep

def receive(s):
    while(True):
        data = s.recv(1024)
        host, port = s.getpeername()
        print(host+":"+data.decode("utf-8"))

def send(s):
    while(True):
        s.sendall(input("msg:").encode("utf-8"))

def th():
    while(True):
        try:
            sh.server(12345,receive)
        except:
            dummy=""
        sleep(1)

t = Thread(target=th)
t.start()

while(input() != "connect"):
    dummy=""

ip = input("ip:")
sh.client(ip,12345,send)
