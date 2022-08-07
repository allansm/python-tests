from Xlib.display import Display
from Xlib import X

from time import sleep

display = Display()
root = display.screen().root

px = 0
py = 0
flag = True

while(True):
    #I dunno why I need this line o.O
    root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType)
    
    gc = root.create_gc(foreground = 0xFF0000, background = 0xFF0000)
    gc2 = root.create_gc(foreground = 0x00FF00, background = 0x00FF00)
    gc3 = root.create_gc(foreground = 0x0000FF, background = 0x0000FF)
    gc4 = root.create_gc(foreground = 0xEEEEEE, background = 0xEEEEEE)
    gc5 = root.create_gc(foreground = 0x222222, background = 0x222222)
    gc6 = root.create_gc()

    root.fill_rectangle(gc6, 0, 0, 520, 520)
    
    root.fill_rectangle(gc, px+0, py+0, 100, 100)
    root.fill_rectangle(gc2, px+100, py+100, 100, 100)
    root.fill_rectangle(gc3, px+0, py+200, 100, 100)
    root.fill_rectangle(gc4, px+100, py+300, 100, 100)
    root.fill_rectangle(gc5, px+200, py+400, 100, 100)
     
    if(px == 200):
        flag = False
    if(px == 0):
        flag = True

    if(flag):
        px+=10
        if(px % 2 == 0):
            py+=1
    else:
        px-=10
        if(px % 2 == 0):
            py-=1
    
    sleep(0.03)
