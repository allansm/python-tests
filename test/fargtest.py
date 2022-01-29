def test():
    print("helloworld")

def test2(txt):
    print(txt)

def test3(func):
    import inspect
    return len(inspect.getfullargspec(func)[0])

def test4(func):
    import inspect
    return inspect.getfullargspec(func)

print(test3(test2))
print(test3(test))
print(test4(test4))
