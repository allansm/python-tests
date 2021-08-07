import tkinter as tk
from tkinter import *
from tkinter import ttk

class Radio:
    def toMiddle(self):
        width, height = self.__root.winfo_reqwidth(), self.__root.winfo_reqheight()

        middlew = str(int(self.__root.winfo_screenwidth()/2-width/2))
        middleh = str(int(self.__root.winfo_screenheight()/2-height/2))

        self.__root.geometry("+"+middlew+"+"+middleh)

    def select(self):
        self.val = self.selected.get()
        self.__root.destroy()

    def __init__(self,arr,title="",root=None):
        if(root == None):
            self.__root = Tk()
            
            self.__root.geometry("400x200")
            self.toMiddle()
             

            container = ttk.Frame(self.__root)
            canvas = tk.Canvas(container)
            scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set)
            
            self.__root.resizable(0,0)

            self.__root.title(title)

            self.selected = IntVar()

            self.selected.set(-1)    

            tmp = lambda win=self.__root,val=self.selected:self.select()
            
            values = self.getOptions(arr)
            for a,b in values:
                ttk.Radiobutton(scrollable_frame,text=a,variable=self.selected,command=tmp,value=b).pack(anchor=W)


            container.pack()
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        else:
            self.__root = root
            
            self.toMiddle()
             
            self.__root = root.window

            container = ttk.Frame(self.__root)
            canvas = tk.Canvas(container)
            scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set)
             
            self.selected = IntVar()

            self.selected.set(-1)    

            tmp = lambda win=self.__root,val=self.selected:self.select()
            
            values = self.getOptions(arr)
            for a,b in values:
                ttk.Radiobutton(scrollable_frame,text=a,variable=self.selected,command=tmp,value=b).pack(anchor=W)


            container.pack()
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            self.__root = root

    def show(self):
        self.__root.mainloop()

    def getOptions(self,arr):
        options = []
        i=0
        for val in arr:
            options.append([val,i])
            i=i+1
        
        return options

