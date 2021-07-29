from tkinter import ALL, EventType
from tkinter import *

def do_zoom(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    factor = 1.001 ** event.delta
    canvas.scale(ALL, x, y, factor, factor)

#root = tk.Tk()
root = Tk()
canvas = Canvas(root,width=1366,height=768)


img = PhotoImage(file=input("image:"))
img.zoom(200,200)
#img.subsample(2)

canvas.create_image(0,0,image=img)


canvas.bind("<MouseWheel>", do_zoom)
canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))

#canvas.pack(fill="both",expand=True)
'''
button3 = Button(root, text="Exit")
button3.pack()
'''
canvas.pack()

root.mainloop()
