import sys
sys.path.append("../functions");
from os import system
from time import sleep
from util import *
import os

command = input("command:")

while True:
    clear()
    system(command)
    sleep(1)
