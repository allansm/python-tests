class Test:
    __txt = None

    def __init__(self,txt):
        self.__txt = txt
    
    def test(self,txt):
        self.__txt += txt

        return self

    def text(self):
        return self.__txt

def test(txt):
    return Test(txt)

text = test("hello").test("world").test("!!!").text()
print(text)
