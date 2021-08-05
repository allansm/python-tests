from tkinter import *

class Cg:
    __maximized = False

    def maximize(self):
        #global maximized
        #global width,height

        if(not self.__maximized):
            self.width, self.height = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
            w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            self.root.geometry("%dx%d+0+0" % (w, h))
            self.__maximized = True

        else:
            self.root.geometry("%dx%d+0+0" % (self.width, self.height))
            self.__maximized = False

    def turnback(self,event):
        #global maximized
        #global width,height

        if(self.__maximized):
            self.root.geometry("%dx%d+0+0" % (width, height))
            self.__maximized = False

    def move_window(self,event):
        self.turnback(self)
        width, height = self.root.winfo_reqwidth(), self.title_bar.winfo_reqheight()
        self.root.geometry('+{0}+{1}'.format(int(event.x_root-width/2), int(event.y_root-height/2)))
        
    def change_on_hovering(event):
        global close_button
        close_button['bg']='red'
        #maximize_button["bg"]="#555555"
    def return_to_normalstate(event):
        global close_button
        close_button['bg']='#2e2e2e'
        #maximize_button["bg"]='#2e2e2e'

    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(True)

        self.title_bar = Frame(self.root, bg='#2e2e2e', bd=2,highlightthickness=0)

        # put a close button on the title bar
        close_button = Button(self.title_bar, text='X', command=self.root.destroy,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)
        maximize_button = Button(self.title_bar, text='☐', command=self.maximize,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',bd = 0,font="bold",fg='white',highlightthickness=0)

        # a canvas for the main area of the window
        window = Canvas(self.root,highlightthickness=0)

        # pack the widgets
        self.title_bar.pack(fill=X)
        close_button.pack(side=RIGHT)
        maximize_button.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)
        xwin=None
        ywin=None
        # bind title bar motion to the move window function
        self.title_bar.bind('<B1-Motion>', self.move_window)
        close_button.bind('<Enter>',self.change_on_hovering)
        close_button.bind('<Leave>',self.return_to_normalstate)
        
        #self.root = root
class Window(Cg().root):
    dummy = ""
cg = Window()

