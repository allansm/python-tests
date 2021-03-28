import fileHandle

print("thing to register:")
register = input()

fileHandle.createFile("register")
fileHandle.writeFile("register",register)

