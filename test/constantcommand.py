from os import system
from time import sleep
import os

command = input("command:")

cls = lambda: system('cls' if os.name=='nt' else 'clear') 

while True:
    cls()
    system(command)
    sleep(1)
