from allansm.downloader import getBytes
from tkinter import *
from PIL import Image,ImageTk
import io

bytes = getBytes(input("url:"))

print(bytes)

root = Tk()

img = Image.open(io.BytesIO(bytes))

w,h = img.size

swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()

if(swidth < w and sheight < h):
    img = img.resize((swidth,sheight))
elif(swidth < w):
    img = img.resize((swidth,h))
elif(sheight < h):
    img = img.resize((w,sheight))

w,h = img.size

canvas = Canvas(root,width=w,height=h,highlightthickness=0)

img = ImageTk.PhotoImage(img)

root.img = canvas.create_image(w/2,h/2,anchor="center",image=img)
canvas.pack()

root.resizable(0, 0)

root.mainloop()
