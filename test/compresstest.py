import zlib
import base65536

i = 0
txt = "Hello World!!!"
temp = txt
while(i < 100):
    tmp = base65536.encode(temp.encode("utf-8"))
    if(len(tmp) < len(txt)):
        print(len(txt))
        print(len(tmp))
        txt = tmp
        i+=1
    else:
        #print(i)
        temp = tmp
        print(temp)

#a = base65536.encode(a.encode("utf-8"))
print(txt)
#print(base65536.decode(a).decode("utf-8"))

'''
bytes = "hello world".encode("utf-8")
tmp = zlib.compress(bytes)
test("a.txt",tmp)
#print(tmp)
tmp = zlib.compress(tmp)
test("b.txt",tmp)
#print(tmp)
tmp = zlib.compress(tmp)
#print(tmp)
test("c.txt",tmp)
'''
