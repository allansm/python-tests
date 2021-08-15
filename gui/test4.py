from tkinter import *

from PIL import Image,ImageTk


def getPercent(val,percent):
    return int(val-(val*percent))

def getImagePercent(image,percent):
    image.resize((getPercent(width,percent),getPercent(height,percent)),Image.ANTIALIAS)

img = Image.open(input("image:"))
root = Tk()

root.geometry("1366x768")

width,height = img.size
print(height)
print(str(int(height-(height*0.25))))

img = img.resize((getPercent(width,0.50),getPercent(height,0.50)),Image.ANTIALIAS)

img = ImageTk.PhotoImage(img)

canvas = Canvas(root,width=1366,height=768)

canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))

canvas.create_image(0,0,image=img)

canvas.pack()

root.mainloop()
