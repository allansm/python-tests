import cv2

cap = cv2.VideoCapture('video.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('', frame)    
    else:
        break

cap.release()

cv2.destroyAllWindows()
