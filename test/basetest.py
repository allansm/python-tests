from base64 import *

def t(txt):
    return txt.encode("utf-8")

def test(txt,x,base):
    for n in range(0,x):
        txt = base(txt)

    print("")
    print(txt.decode("utf-8"))

    return txt.decode("utf-8")

print(b85encode(t("helloworld")))
print(b64encode(t("helloworld")))
print(b32encode(t("helloworld")))
print(b16encode(t("helloworld")))

a = test(t("abc"),5,b85encode)
b = test(t("abc"),4,b64encode)
c = test(t("abc"),3,b32encode)
d = test(t("abc"),2,b16encode)

test(t(a),5,b85decode)
test(t(b),4,b64decode)
test(t(c),3,b32decode)
test(t(d),2,b16decode)
