import os
import signal
from os import getpid

pid = getpid()

print(pid)

os.kill(pid, signal.SIGTERM)

while(True):
    print("fail")
