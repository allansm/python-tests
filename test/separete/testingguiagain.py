from tkinter import *

global maximized
global width,height

maximized = False

def maximize(event):
    global maximized
    global width,height

    if(not maximized):
        width, height = root.winfo_reqwidth(), root.winfo_reqheight()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        maximized = True
    else:
        root.geometry("%dx%d+0+0" % (width, height))
        maximized = False

def turnback():
    global maximized
    global width,height

    if(maximized):
        root.geometry("%dx%d+0+0" % (width, height))
        maximized = False


def move_window(event):
    turnback()
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    

trueroot = Tk()
trueroot.attributes('-alpha', 0.0)
trueroot.title("")

root = Tk()

root.overrideredirect(True)
root.bind('<B1-Motion>', move_window)
root.bind("<Double-Button>",maximize)


root.mainloop()
