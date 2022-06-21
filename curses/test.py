import curses
from curses import wrapper
from curses.textpad import Textbox

from allansm.file import *

def main(screen):
    txt = File(".txt")
    
    if(not txt.exists()):
        txt.write("")

    screen.border(0)
    
    win = curses.newwin(0,0, 0,0)
     
    win.addstr(0, 0, txt.read())
    win.refresh()
    
    box = Textbox(win)
    
    box.edit()
    
    txt.write(box.gather())

wrapper(main)
