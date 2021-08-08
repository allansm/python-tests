from custom import *
from ask import *
from radio import *

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

def test2():
    root = root()
    root.size(200,150)
    root.topbarbg("#00f")
    root.window["bg"] = "#eee"
    root.maximize.pack_forget()

    entry = Ask("name:","",root)
    entry.show()

    print(entry.val)
def test3():
    test = root()
    test.size(200,150)
    test.topbarbg("#000","#fff")
    test.window["bg"] = "#fff"
    test.maximize.pack_forget()

    arr = ["aaa","bbb"]
    radio = Radio(arr,"",test)
    radio.toMiddle()
    radio.show()

    print(arr[radio.val])

test3()
'''exit()
root = Tk()
#hide = Toplevel(root)
root.overrideredirect(True)
root.iconphoto(False, PhotoImage(file="app.png"))
root.attributes("-alpha",0.0)

root.bind("<FocusIn>",root.attributes("-alpha",0.0))
root.bind("<FocusIn>",root.attributes("-topmost",1))

root.mainloop()'''
'''
root = Tk()
hide = Tk()
hide.bind("<FocusOut>",root.overrideredirect(False)) 
hide.bind("<FocusIn>",root.overrideredirect(True))
root.overrideredirect(True)

root.mainloop()'''
