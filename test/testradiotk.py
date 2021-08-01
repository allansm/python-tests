from tkinter import *


def select(root,selected):
    global val
    val = selected.get()
    root.destroy()
    return val

def radio(values):
    root = Tk()

    selected = IntVar()

    selected.set(-1)
    
    tmp = lambda win=root,val=selected:select(win,val)

    for a,b in values:
        Radiobutton(root,text=a,padx=20,variable=selected,command=tmp,value=b).pack()

    root.mainloop()

    return val


values = []

values.append(["test",1])

val = radio(values)

print(val)
