import cv2

from allansm.imageHandle import *
from tkinter import *
from threading import *

root = Tk()
canvas = Canvas(root,width=1366,height=768,highlightthickness=0)
canvas.pack()

def test():
    from time import sleep
    from PIL import Image,ImageTk

    cap = cv2.VideoCapture(input("video:"))

    global canvas

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)

            canvas.create_image(1366/2,768/2,image=img)
            lastimg = img
        else:
            break

    cap.release()

    cv2.destroyAllWindows()

t = Thread(target=test)
t.start()

root.mainloop()
