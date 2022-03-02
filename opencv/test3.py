from PIL import Image
from os import mkdir,chdir
import cv2

try:
    mkdir("test")
except:
    error=0

chdir("test")

cap = cv2.VideoCapture(input("video:"))

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        
        print(str(i)+".png")
        img.save(str(i)+".png","png")
        i+=1
    else:
        break

cap.release()

cv2.destroyAllWindows()
