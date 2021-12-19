from tkinter import *

root = Tk()

x = root.winfo_pointerx()
y = root.winfo_pointery()
absx = root.winfo_pointerx() - root.winfo_rootx()
absy = root.winfo_pointery() - root.winfo_rooty()

print(absx)
print(absy)
