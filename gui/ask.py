from tkinter import *
from tkinter import ttk

class Ask:
    val = ""

    def toMiddle(self):
        width, height = self.__root.winfo_reqwidth(), self.__root.winfo_reqheight()

        middlew = str(int(self.__root.winfo_screenwidth()/2-width/2))
        middleh = str(int(self.__root.winfo_screenheight()/2-height/2))

        self.__root.geometry("+"+middlew+"+"+middleh)

    def getEntry(self,event=None):
        self.val = self.__entry.get()
        self.__root.destroy() 

    def show(self):
        self.__root.mainloop()

    def __init__(self,labeltext,title="",root=None):
        if(root == None):
            self.__root = Tk()

            self.__root.option_add("*tearOff", False)

            self.__root.geometry("200x130")
            self.toMiddle()
            
            self.__root.title(title)

            self.__root.resizable(0,0)

            label = ttk.Label(self.__root, text=labeltext)
            label.pack()

            label.place(x=25,y=10)

            self.__entry = ttk.Entry(self.__root,width=23)
            self.__entry.pack()

            self.__entry.place(x=25,y=35)
            

            button = ttk.Button(self.__root,text="Ok",width=5,command=self.getEntry)
            button.pack()

            button.place(x=25,y=85)
            
            self.__root.bind("<Return>",self.getEntry)

        else:
            self.__root = root

            self.__root.option_add("*tearOff", False)
 
            self.toMiddle()

            self.__root.resizable(0,0)
            window = self.__root.window
            label = ttk.Label(window, text=labeltext)
            label.pack()

            label.place(x=25,y=10)

            self.__entry = ttk.Entry(window,width=23)
            self.__entry.pack()

            self.__entry.place(x=25,y=35)
            

            button = ttk.Button(window,text="Ok",width=5,command=self.getEntry)
            button.pack()

            button.place(x=25,y=85)
            
            self.__root.bind("<Return>",self.getEntry)


