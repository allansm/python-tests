import winsound
i = 37
ii = 1

while True:
    winsound.Beep(i, ii)
    i= i+100
    ii = ii+15
    if(i >= 32767):
        break
