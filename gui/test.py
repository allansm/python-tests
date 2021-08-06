from custom import *
from guientry import *

def test1():
    root = root()

    root.topbarbg("#111")
    root.window["bg"] = "#111"
    root.window.bind("<B1-Motion>",root.custom.move_window)

    entry = Entry(root.window)
    button = Button(root.window,text="button")

    entry.pack()
    entry.place(x=25,y=25)
    button.pack()
    button.place(x=170,y=20)

    root.geometry("250x120")

    root.mainloop()

root = root()
root.size(200,150)
root.topbarbg("#00f")
root.window["bg"] = "#eee"
#root.maximize.pack_forget()

entry = GuiEntry("name:","",root)
entry.show()

print(entry.val)
