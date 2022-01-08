from tkinter import *
x = 0
y = 0
x1 = None
y1 = None

def test(event):
    global x,y,x1,y1
    
    if(event.x > x1):
        x = event.x-x1
    else:
        x= (x1-event.x)*-1
    x1 = event.x
    print(x)
    canvas.move("rect",x,0)
     
    if(event.y > y1):
        y = event.y-y1
    else:
        y= (y1-event.y)*-1
    y1 = event.y
    print(y)
    canvas.move("rect",0,y)

def test2(event):
    global x1,y1

    x1 = event.x
    y1 = event.y

root = Tk()
root.geometry("400x300")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

rect = canvas.create_rectangle(0, 0, 50, 50, fill='red',tag='rect')

canvas.tag_bind("rect","<B1-Motion>",test)
canvas.tag_bind("rect","<Button-1>",test2)
root.mainloop()
