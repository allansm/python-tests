from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

original = None

try:
    path = askopenfilename()

    print(path)

    original = Image.open(path)
except:
    exit()

root.title("posterize")
root.geometry("800x600")

canvas = Canvas(root, width=800, height=600, highlightthickness=0)
canvas.config(bg="black")
canvas.pack(fill="both", expand=True)

colors = 16
grayscale = False

image = original.resize((800,600)).quantize(colors=colors, method=2)

img = ImageTk.PhotoImage(image)

canvas.create_image(800/2, 600/2, image=img)

def l(event):
    global colors, original, image, img, canvas, grayscale
    
    if(colors > 1):
        colors-=1
        
        print(str(colors)+" colors")
        
        image = original.resize((800,600)).quantize(colors=colors, method=2)
        
        if(grayscale):
            image = image.convert("L")
        
        img = ImageTk.PhotoImage(image)
        canvas.create_image(800/2, 600/2, image=img)

def r(event):
    global colors, original, image, img, canvas, grayscale
    
    if(colors <= 255):
        colors+=1
        
        print(str(colors)+" colors")
        
        image = original.resize((800,600)).quantize(colors=colors, method=2)
        
        if(grayscale):
            image = image.convert("L")

        img = ImageTk.PhotoImage(image)
        canvas.create_image(800/2, 600/2, image=img)

def space(event):
    global colors, original, image, img, canvas, grayscale

    if(grayscale):
        grayscale = False
    else:
        grayscale = True

    image = original.resize((800,600)).quantize(colors=colors, method=2)
    
    if(grayscale):
        image = image.convert("L")

    img = ImageTk.PhotoImage(image)
    canvas.create_image(800/2, 600/2, image=img)

def open(event):
    global colors, original, image, img, canvas, grayscale, original

    path = askopenfilename()
    if(path != None and path != ""):
        print(path)

        original = Image.open(path)

    image = original.resize((800,600)).quantize(colors=colors, method=2)
    
    if(grayscale):
        image = image.convert("L")

    img = ImageTk.PhotoImage(image)
    canvas.create_image(800/2, 600/2, image=img)

root.bind("<Left>", l)
root.bind("<Right>", r)
root.bind("<KeyPress-space>", space)
root.bind("<KeyPress-o>", open)

root.resizable(0, 0)
root.eval('tk::PlaceWindow . center')

root.after(1, lambda: root.focus_force())

root.mainloop()

if(askyesno(title="", message="Save?")):
    image = original.quantize(colors=colors, method=2)
    
    if(grayscale):
        image = image.convert("L")
    
    image.save("output.png")

