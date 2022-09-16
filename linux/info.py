from proc import *
from os import system
import os
from time import sleep

import curses
from curses import wrapper
from curses.textpad import Textbox
import sys

def getRam():
    out = check_output("free | grep Mem | awk '{print $3/$2 * 100.0}'", shell=True).decode()
    out = float(out.replace("\n", "").replace(",", "."))
    return out

def bar(n, percent):
    bar = n+" "+("█"*round(percent/5))+("░"*round((100-percent)/5))+" "+("{:.3}".format(percent))+"%"
    return bar

ms = 0.1

try:
    ms = float(str(sys.argv[1]))
except:
    pass

stdscr = curses.initscr()

while(True):
    try:
        cpu = bar("cpu", getCpu()["total in use"])
        ram = bar("ram", getRam())
        lines = curses.LINES//2
        stdscr.addstr((lines//2), curses.COLS//2-(len(cpu)//2), cpu)
        stdscr.addstr((lines//2)+2, curses.COLS//2-(len(ram)//2), ram)
        
        stdscr.refresh()
        
        sleep(ms)
        
        stdscr.clear()
    except:
        stdscr = curses.initscr()
