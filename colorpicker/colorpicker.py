from tkinter import *
from PIL import ImageGrab

root = Tk()

x = root.winfo_pointerx() - root.winfo_rootx()
y = root.winfo_pointery() - root.winfo_rooty()

screen = ImageGrab.grab()
px = screen.getpixel((x, y))

print(x, end=" ")
print(y, end=" ")
print(px, end=" ")
print('#%02x%02x%02x' % px)
