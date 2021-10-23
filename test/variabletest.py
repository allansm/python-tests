def test():
    class dunno():
        __dummy = ""

    abst = dunno()
    abst.text = "hello"
    abst.text2 = " world"

    return abst

print(test().text+test().text2)
