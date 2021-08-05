from testingcustomgui2 import root as window
root = window()

root.close["bg"] = "red"
root.maximize["bg"] = "red"
root.topbar["bg"] = "red"
root.geometry("400x100")
root.mainloop()
