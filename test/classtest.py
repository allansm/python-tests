class Test:
    publicVal = "public"
    _protectedVal = "protected"
    __privateVal = "private"

    def __init__(self,test):
        self.test = test

    def helloworld(self):
        print("helloworld")
    
    def print(self,txt):
        print(txt)

class Test2:
    def test(self):
        from os import system
        system("dir")

t = Test("test")

t.print(t.test)

t2 = Test2()

t2.test()
