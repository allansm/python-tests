
import tkinter as tk


root=tk.Tk()

root.overrideredirect(1)

#txt = StringVar()

#txt.set("helloworld")

label = tk.Label(root,bg="systemTransparent", text="helloworld")
root.overrideredirect(True)
root.geometry("+250+250")
#root.lift()
root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True)
#root.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()
