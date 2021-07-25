
from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 800, height = 600)      
            
canvas.pack()      
img = PhotoImage(file="ppt.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()
