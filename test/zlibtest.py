import zlib

data = "121212121212121212121212121212121212121212121212121212121212121212121212121212121212121"

for n in range(1,10):
    test = zlib.compress(data.encode(),n)
    print(test)
    #print(zlib.decompress(test))
