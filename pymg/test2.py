import sys
sys.path.append("../functions")
sys.path.append("../gui")

from tkinter import * 
from tkinter import ALL, EventType
from tkinter import ttk

from argsHandle import *
import custom
import util
import fileHandle

root = util.do(lambda : custom.root(),fileHandle.selfLocation(__file__)+"/icon")

root.option_add("*tearOff", False)

canvas = Canvas(root.window,width=root.winfo_screenwidth(),height=root.winfo_screenheight(),highlightthickness=0)

middle = int(root.winfo_screenwidth()/2-45)

canvas.configure(background='#111')

root.canvas = canvas
root.canvas.pack()

img = PhotoImage(file=getArgs(["image"]).image)
root.canvas.img = canvas.create_image(0,0,image=img)

root.canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
root.canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))

root.topbarbg("#111")
root["bg"] = "#111"

root.size(800,600) 
root.minsize(640, 480)
root.mainloop() 

