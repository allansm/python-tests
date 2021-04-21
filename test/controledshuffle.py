from random import shuffle

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def fakeshuffle(arr):
    h1,h2 = split_list(arr)

    a,b = split_list(h1)
    c,d = split_list(h2)

    shuffle(a)
    shuffle(b)
    shuffle(c)
    shuffle(d)

    arr = a+b+c+d

    return arr

array = [1,2,3,4,5,6,7,8,9,10]

arr = fakeshuffle(array)

for n in arr:
    print(n)
