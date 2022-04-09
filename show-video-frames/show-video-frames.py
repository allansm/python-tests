from tkinter.filedialog import askopenfilename as openfile
from tkinter import *
from allansm.opencv import *
from PIL import Image, ImageTk

def l(event):
    global current, frames, canvas, lastimg

    current-=1

    if(current < 0):
        current = 0
    
    img = Image.fromarray(frames[current])
    img = ImageTk.PhotoImage(img)
    canvas.create_image(1366/2, 768/2, image=img)
    
    lastimg = img

    print("frame:"+str(current))

def r(event):
    global current, frames, canvas, lastimg

    current+=1

    if(current > len(frames)):
        current = len(frames)
    
    img = Image.fromarray(frames[current])
    img = ImageTk.PhotoImage(img)
    canvas.create_image(1366/2, 768/2, image=img)
    
    lastimg = img

    print("frame:"+str(current))

lastimg = None
current = 0

root = Tk()

file = openfile()
frames = getFrames(file)

print(len(frames))

canvas = Canvas(root, width=1366, height=768, highlightthickness=0)
canvas.pack(fill="both", expand=True)

img = Image.fromarray(frames[0])
img = ImageTk.PhotoImage(img)

canvas.create_image(1366/2, 768/2, image=img)

root.bind("<Left>", l)
root.bind("<Right>", r)
root.after(1, lambda: root.focus_force())

root.mainloop()
