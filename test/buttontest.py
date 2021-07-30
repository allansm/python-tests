from tkinter import *

def test(event):
    print("helloworld")


root = Tk()

button = Button(text="execute")
button.bind("<Button-1>", test)

button.pack()

root.mainloop()
