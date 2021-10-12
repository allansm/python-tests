import tkinterweb
import tkinter as tk
root = tk.Tk()

def move_window(event):
    root.geometry('+{0}+{1}'.format(int(event.x_root), int(event.y_root)))

root.bind('<B1-Motion>',move_window)


root.overrideredirect(True)

frame = tkinterweb.HtmlFrame(root)
frame.load_website("www.google.com")
frame.pack(fill="both", expand=True)
root.mainloop()
