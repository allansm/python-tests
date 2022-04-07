from tkinter.filedialog import askopenfilename as openfile
from tkinter import *
from allansm.opencv import *
from PIL import Image, ImageTk

def l(event):
    global current, frames, canvas

    current-=1

    if(current < 0):
        current = 0
    
    img = Image.fromarray(frames[current])
    img = ImageTk.PhotoImage(img)
    canvas.create_image(1366/2, 768/2, image=img)
    
    print("frame:"+str(current))

def r(event):
    global current, frames, canvas

    current+=1

    if(current > len(frames)):
        current = len(frames)
    
    img = Image.fromarray(frames[current])
    img = ImageTk.PhotoImage(img)
    canvas.create_image(1366/2, 768/2, image=img)
    
    print("frame:"+str(current))

current = 0

root = Tk()

file = openfile()
frames = getFrames(file)
print(len(frames))

canvas = Canvas(root, width=1366, height=768, highlightthickness=0)
canvas.pack()

img = Image.fromarray(frames[0])
img = ImageTk.PhotoImage(img)

canvas.create_image(1366/2, 768/2, image=img)

root.bind("<Left>", l)
root.bind("<Right>", r)

root.mainloop()
