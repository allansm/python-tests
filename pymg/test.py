import sys
sys.path.append("../functions")

from argsHandle import *

from tkinter import *   
from os import chdir

root = Tk()      
canvas = Canvas(root, width = 1366, height = 768)      
            
canvas.pack()
args = getArgs(["image"])

image = args.image

img = PhotoImage(file=image)      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()
