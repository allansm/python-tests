from tkinter import *

class Cg:
    __maximized = False
    __root = ""

    def maximize(self):
        if(not self.__maximized):
            self.width, self.height = self.__root.winfo_reqwidth(), self.__root.winfo_reqheight()
            w, h = self.__root.winfo_screenwidth(), self.__root.winfo_screenheight()
            self.__root.geometry("%dx%d+0+0" % (w, h))
            self.__maximized = True

        else:
            self.__root.geometry("%dx%d+0+0" % (self.width, self.height))
            self.__maximized = False

    def turnback(self,event):
        if(self.__maximized):
            self.__root.geometry("%dx%d+0+0" % (width, height))
            self.__maximized = False

    def move_window(self,event):
        self.turnback(self)
        width, height = self.__root.winfo_reqwidth(), self.__root.topbar.winfo_reqheight()
        self.__root.geometry('+{0}+{1}'.format(int(event.x_root-width/2), int(event.y_root-height/2)))
        
    def change_on_hovering(self,event):
        self.__root.close['bg']='red'
        
    def return_to_normalstate(self,event):
        self.__root.close['bg']='#2e2e2e' 

    def __init__(self):
        self.__root = Tk()
        self.__root.overrideredirect(True)

        self.__root.topbar = Frame(self.__root, bg='#2e2e2e', bd=2,highlightthickness=0)
 
        self.__root.close = Button(self.__root.topbar, text='X', command=self.__root.destroy,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)
        self.__root.maximize = Button(self.__root.topbar, text='☐', command=self.maximize,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)

        self.__root.window = Canvas(self.__root,highlightthickness=0)
 
        self.__root.topbar.pack(fill=X)
        self.__root.close.pack(side=RIGHT)
        self.__root.maximize.pack(side=RIGHT)
        self.__root.window.pack(expand=1, fill=BOTH)
        xwin=None
        ywin=None
        
        self.__root.topbar.bind('<B1-Motion>', self.move_window)
        self.__root.close.bind('<Enter>',self.change_on_hovering)
        self.__root.close.bind('<Leave>',self.return_to_normalstate)
 
    def show(self):
        self.__root.mainloop()
    
    def getRoot(self):
        self.__root.cg = self
        return self.__root

def root():
    return Cg().getRoot()
