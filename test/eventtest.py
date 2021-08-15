from tkinter import *

def test(event):
    if event.num == 5 or event.delta == -120:
        print("down")
    
    if event.num == 4 or event.delta == 120:
        print("up")

root = Tk()

root.bind("<MouseWheel>",test)

root.mainloop()
