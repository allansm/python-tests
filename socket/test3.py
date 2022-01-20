import sys
sys.path.append("../../python-lib")

from allansm.socketHandle import *
from allansm.file import *

def run(s):
    send(s,"...")
    recv = receive(s,True)
    print(recv)

client("127.0.0.1",54321,run)
