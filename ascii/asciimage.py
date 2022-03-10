def toAscii(img,w,h,arr):
    last = 0
    
    image = ""
    
    img = img.resize((w,h))

    for y in range(0,h):
        for x in range(0,w):
            px = img.getpixel((x,y))
            if(px != last):
                last = px

            image+=arr[px%len(arr)]
        
        image+="\n"
    
    return image
