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

t = Test("test")

t.print(t.test)
