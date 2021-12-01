import sys
sys.path.append("../../python-lib")

import pyautogui
from elapse import *

e = Elapse()
i = 0
while(e.elapsed() < 1000):
    a = pyautogui.screenshot()#region=(0,0,100,100))
    a.save("test.png")
    i+=1

print(i)
