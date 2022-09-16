from proc import *
from os import system
import os
from time import sleep

import curses
from curses import wrapper
from curses.textpad import Textbox

def getRam():
    out = check_output("free | grep Mem | awk '{print $3/$2 * 100.0}'", shell=True).decode()
    out = float(out.replace("\n", "").replace(",", "."))
    return out

def getCpu():
    out = check_output("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'", shell=True).decode()
    out = float(out.replace("\n", "").replace(",", "."))
    return out
 
def bar(n, percent):
    bar = n+" "+("█"*round(percent/5))+("░"*round((100-percent)/5))+" "+("{:.3}".format(percent))+"%"
    return bar

stdscr = curses.initscr()

while(True):
    try:
        cpu = bar("cpu", getCpu())
        ram = bar("ram", getRam())
        lines = curses.LINES//2
        stdscr.addstr((lines//2), curses.COLS//2-(len(cpu)//2), cpu)
        stdscr.addstr((lines//2)+2, curses.COLS//2-(len(ram)//2), ram)
        
        stdscr.refresh()
        
        sleep(0.1)
        
        stdscr.clear()
    except:
        stdscr = curses.initscr()
