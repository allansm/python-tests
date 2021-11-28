import zlib
import base65536

i = 0
txt = "Hello World!!!"
txt2 = txt.encode("utf-8")

txt = txt.encode("utf-8")
print(txt)
txt = zlib.compress(txt)
print(txt)
txt = base65536.encode(txt)

print(txt)
print(base65536.encode(txt2))
