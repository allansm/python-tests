import zlib

def test(fname,b):
    f = open(fname,"wb")
    f.write(b)
    f.close()

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

