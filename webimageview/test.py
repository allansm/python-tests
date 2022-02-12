from allansm.downloader import getBytes
from tkinter import *
from PIL import Image,ImageTk
import io

bytes = getBytes(input("url:"))

print(bytes)

root = Tk()

canvas = Canvas(root,width=1366,height=768,highlightthickness=0)

img = Image.open(io.BytesIO(bytes))
img = ImageTk.PhotoImage(img)

canvas.create_image(1366/2,768/2,anchor="center",image=img)
canvas.pack()
root.mainloop()
