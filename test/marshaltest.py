import marshal

data = 10

bytes = marshal.dumps(data)
eggs = marshal.loads(bytes)

print(eggs)
