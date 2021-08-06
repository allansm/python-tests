from testingcustomgui2 import root as window
root = window()

root.close["bg"] = "blue"
root.maximize["bg"] = "blue"
root.topbar["bg"] = "blue"
root.geometry("800x600")

root.mainloop()
