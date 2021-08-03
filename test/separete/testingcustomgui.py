from tkinter import *

global maximized
global width,height

maximized = False

def maximize():
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



#trueroot = Tk()
#trueroot.attributes('-alpha', 0.0)
#trueroot.title("")

root = Tk()
root.overrideredirect(True) # turns off title bar, geometry
#root.geometry('400x100+200+200') # set new geometry

# make a frame for the title bar
title_bar = Frame(root, bg='#2e2e2e', bd=2,highlightthickness=0)

# put a close button on the title bar
close_button = Button(title_bar, text='X', command= root.destroy,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)
maximize_button = Button(title_bar, text='☐', command=maximize,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)

# a canvas for the main area of the window
window = Canvas(root,highlightthickness=0)

# pack the widgets
title_bar.pack(fill=X)
close_button.pack(side=RIGHT)
maximize_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)
xwin=None
ywin=None
# bind title bar motion to the move window function

def move_window(event):
    turnback()
    width, height = root.winfo_reqwidth(), title_bar.winfo_reqheight()
    root.geometry('+{0}+{1}'.format(int(event.x_root-width/2), int(event.y_root-height/2)))
    
def change_on_hovering(event):
    global close_button
    close_button['bg']='red'
    #maximize_button["bg"]="#555555"
def return_to_normalstate(event):
    global close_button
    close_button['bg']='#2e2e2e'
    #maximize_button["bg"]='#2e2e2e'

title_bar.bind('<B1-Motion>', move_window)
close_button.bind('<Enter>',change_on_hovering)
close_button.bind('<Leave>',return_to_normalstate)

test = Entry(window,width=50)
test.pack()
test.place(x=0,y=0)
root.mainloop()
