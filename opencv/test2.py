import cv2

from allansm.imageHandle import *
from tkinter import *
from threading import *

root = Tk()
canvas = Canvas(root,width=640,height=480,highlightthickness=0)
canvas.pack()

def test():
    from time import sleep
    from PIL import Image,ImageTk

    cap = cv2.VideoCapture(input("video:"))

    global canvas
    frames = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize((640,480)) 
            frames.append(img)
            
        else:
            break
    
    cap.release()
    
    cv2.destroyAllWindows()
    
    for img in frames:
        img = ImageTk.PhotoImage(img)
        canvas.create_image(640/2,480/2,image=img)
        lastimg = img
        
        frames = []

t = Thread(target=test)
t.start()

root.mainloop()
