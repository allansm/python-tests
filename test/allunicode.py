for i in range(0, 144698):
    x = chr(i)
    
    try:
        print(x.encode())
    except:
        dummy=""
    
    print(ord(x))
