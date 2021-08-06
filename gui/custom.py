from tkinter import *

class Custom:
    __maximized = False
    __root = ""

    def maximize(self):
        if(not self.__maximized):
            #self.width, self.height = self.__root.winfo_reqwidth(), self.__root.winfo_reqheight()
            w, h = self.__root.winfo_screenwidth(), self.__root.winfo_screenheight()
            self.__root.geometry("%dx%d+0+0" % (w, h))
            self.__maximized = True

        else:
            self.__root.geometry("%dx%d+0+0" % (self.width, self.height))
            self.__maximized = False

    def turnback(self,event):
        if(self.__maximized):
            self.__root.geometry("%dx%d+0+0" % (self.width, self.height))
            self.__maximized = False

    def move_window(self,event):
        self.turnback(self)
        #width, height = self.__root.winfo_reqwidth(), self.__root.topbar.winfo_reqheight()
        self.__root.geometry('+{0}+{1}'.format(int(event.x_root-self.width/2), int(event.y_root-self.topbarheight/2))) 
    
    def change_on_hovering(self,event):
        self.__root.close['bg']='red'
        
    def return_to_normalstate(self,event):
        self.__root.close['bg']=self.__root.topbar["bg"]

    def handle_focus(self,event):
        self.__root.attributes("-topmost",True)
        self.__root.attributes("-topmost",False)
    
    def topbarbg(self,color):
        self.__root.topbar["bg"] = color
        self.__root.close["bg"] = color
        self.__root.maximize["bg"] = color
    
    def size(self,width,height):
        self.__root.geometry(str(width)+"x"+str(height))
        self.width, self.height = width, height

    def __init__(self):
        self.__root = Tk()
        self.__root.title("")
        self.__root.overrideredirect(True)
        
        hide = Toplevel(self.__root)
        hide.bind("<FocusIn>",self.handle_focus)      
        hide.attributes("-alpha",0.0) 

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
        
        self.__root.topbarbg = self.topbarbg
        self.__root.size = self.size
        
        self.width, self.height = self.__root.winfo_reqwidth(), self.__root.winfo_reqheight()
        self.topbarheight = self.__root.topbar.winfo_reqheight()

    def show(self):
        self.__root.mainloop()
    
    def getRoot(self):
        self.__root.custom = self
        return self.__root

def root():
    return Custom().getRoot()


