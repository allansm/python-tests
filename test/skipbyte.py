bytes = b"helloworld"

i = 0
test = []
for n in bytes:
    if(i == 5):
        test.append(n)
    else:
        i+=1

print(bytearray(test).decode())
