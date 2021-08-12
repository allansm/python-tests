from tkinter import *

class Custom:
    __maximized = False
    __root = ""
    __minimized = False
    __fix = True
    __canMove = True

    def maximize(self):
        if(not self.__maximized):
            w, h = self.__root.winfo_screenwidth(), self.__root.winfo_screenheight()
            self.__root.geometry("%dx%d+0+0" % (w, h))
            self.__maximized = True

        else:
            self.__root.geometry("%dx%d+0+0" % (self.width, self.height))
            self.__maximized = False
    def minimize(self):
        self.__root.withdraw()
        self.__minimized = True
        if(self.__fix == False):
            self.__fix = True
        else:
            self.__fix = False

    def turnback(self,event):
        if(self.__maximized):
            self.__root.geometry("%dx%d+0+0" % (self.width, self.height))
            self.__maximized = False

    def move_window(self,event):
        if(self.__canMove):
            self.turnback(self)
            self.__root.geometry('+{0}+{1}'.format(int(event.x_root-self.width/2), int(event.y_root-self.topbarheight/2))) 
    
    def change_on_hovering(self,event):
        self.__root.close['bg']='red'
        
    def return_to_normalstate(self,event):
        self.__root.close['bg']=self.__root.topbar["bg"]

    def handle_focus(self,event):
        self.__root.attributes("-topmost",True)
        self.__root.attributes("-topmost",False)

        if(self.__minimized):
            if(self.__fix):
                self.__fix = False
            else:
                self.__root.deiconify()
                self.__minimized = False

    def topbarbg(self,bg="#2e2e2e",fg="white"):
        self.__root.topbar["bg"] = bg
        self.__root.close["bg"] = bg
        self.__root.maximize["bg"] = bg
        self.__root.minimize["bg"] = bg
        self.__root.title["bg"] = bg
        
        self.__root.close["fg"] = fg
        self.__root.maximize["fg"] = fg
        self.__root.minimize["fg"] = fg
        self.__root.title["fg"] = fg



    def size(self,width,height):
        self.__root.geometry(str(width)+"x"+str(height))
        self.width, self.height = width, height

    def __init__(self,title=""):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.overrideredirect(True)
        self.__root.iconphoto(False, PhotoImage(file="app.png"))

        hide = Toplevel(self.__root)
        hide.bind("<FocusIn>",self.handle_focus)      
        hide.attributes("-alpha",0.0) 
        hide.iconphoto(False, PhotoImage(file="app.png"))

        self.__root.topbar = Frame(self.__root, bg='#2e2e2e', bd=2,highlightthickness=0)
 
        self.__root.close = Button(self.__root.topbar, text='X', command=self.__root.destroy,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)
        self.__root.maximize = Button(self.__root.topbar, text='☐', command=self.maximize,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)
        self.__root.minimize = Button(self.__root.topbar, text='— ', command=self.minimize,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)

        self.__root.title = Label(self.__root.topbar,text=title,bg = "#2e2e2e",fg="white")
        self.__root.window = Canvas(self.__root,highlightthickness=0)
 
        self.__root.topbar.pack(fill=X)
        self.__root.close.pack(side=RIGHT)
        self.__root.maximize.pack(side=RIGHT)
        self.__root.minimize.pack(side=RIGHT)
        self.__root.title.pack(side=LEFT)
        self.__root.window.pack(expand=1, fill=BOTH)
        xwin=None
        ywin=None
        
        self.__root.topbar.bind('<B1-Motion>', self.move_window)
        #test
        self.__root.topbar.bind("<Double-Button-1>",lambda event : self.maximize())

        self.__root.close.bind('<Enter>',self.change_on_hovering)
        self.__root.close.bind('<Leave>',self.return_to_normalstate)
        
        self.__root.topbarbg = self.topbarbg
        self.__root.size = self.size
        self.__root.canMove = self.setCanMove

        self.width, self.height = self.__root.winfo_reqwidth(), self.__root.winfo_reqheight()
        self.topbarheight = self.__root.topbar.winfo_reqheight()

    def show(self):
        self.__root.mainloop()
    
    def getRoot(self):
        self.__root.custom = self
        return self.__root
    
    def setCanMove(self,canMove):
        self.__canMove = canMove

def root(title=""):
    return Custom(title).getRoot()


