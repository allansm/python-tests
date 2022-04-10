from tkinter.filedialog import askopenfilename as openfile
from tkinter import *
from allansm.opencv import *
from PIL import Image, ImageTk

def size(event):
    global current, frames, canvas, lastimg, root
    
    img = getFrame(frames[current])
    img = getImage(img)

    w, h = img.size
    while(w > root.winfo_width()):    
        img = img.resize((int(w*0.9), int(h*0.9)))
        w, h = img.size

    img = ImageTk.PhotoImage(img)
    
    canvas.delete('all')
    canvas.config(width=root.winfo_width(), height=root.winfo_height())
    canvas.create_image(root.winfo_width()/2, root.winfo_height()/2, image=img)
     
    lastimg = img

def l(event):
    global current, frames, canvas, lastimg, root

    current-=1

    if(current < 0):
        current = 0
    
    img = getFrame(frames[current])
    img = getImage(img)

    w, h = img.size
    while(w > root.winfo_width()):    
        img = img.resize((int(w*0.9), int(h*0.9)))
        w, h = img.size

    img = ImageTk.PhotoImage(img)
    
    canvas.delete('all')
    canvas.config(width=root.winfo_width(), height=root.winfo_height())
    canvas.create_image(root.winfo_width()/2, root.winfo_height()/2, image=img)
     
    lastimg = img

    print("frame:"+str(current))

def r(event):
    global current, frames, canvas, lastimg, root

    current+=1

    if(current > len(frames)-1):
        current = len(frames)-1
    
    img = getFrame(frames[current])
    img = getImage(img)

    w, h = img.size
    while(w > root.winfo_width()):    
        img = img.resize((int(w*0.9), int(h*0.9)))
        w, h = img.size

    img = ImageTk.PhotoImage(img)
    
    canvas.delete('all')
    canvas.config(width=root.winfo_width(), height=root.winfo_height())
    canvas.create_image(root.winfo_width()/2, root.winfo_height()/2, image=img)
    
    lastimg = img

    print("frame:"+str(current))

lastimg = None
current = 0

root = Tk()
root.title("show-video-frames")
root.geometry("640x480")

file = openfile()
frames = getFrames(file)

print(len(frames))

canvas = Canvas(root, width=640, height=480, highlightthickness=0)
canvas.config(bg="black")
canvas.pack(fill="both", expand=True)

img = getFrame(frames[0])
img = getImage(img)

w, h = img.size
while(w > root.winfo_width()):    
    img = img.resize((int(w*0.9), int(h*0.9)))
    w, h = img.size    

img = ImageTk.PhotoImage(img)

canvas.create_image(640/2, 480/2, image=img)

root.bind("<Left>", l)
root.bind("<Right>", r)
root.bind("<Configure>", size)

root.after(1, lambda: root.focus_force())

root.mainloop()
