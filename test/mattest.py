from random import shuffle
from random import randrange
def removed():
    arr1 = [1,2,3,4,5]
    arr2 = [6,7,8]

    mat = [arr1,arr2]
    arr3 = [0,0]
    total = len(arr1+arr2)

    print("total "+str(total))

    i = 0

    while(i <= total):
        i = i + 1
        try:
            index = randrange(0,len(mat))
            val = mat[index][arr3[index]]
            arr3[index] = arr3[index] + 1
            #print("index "+str(index))
            print(val)
        except:
            dummy = ""
    #shuffle(arr1)
    #shuffle(arr2)

    #print(arr1)
    #print(arr2)

def test(mat):
    total = 0
    indexs = []
    for m in mat:
        total = total + len(m)
        indexs.append(0)

    i = 0
    while(i < total):
        try:
            index = randrange(0,len(mat))
            val = mat[index][indexs[index]]
            indexs[index] = indexs[index] + 1

            print(val)
            i = i +1
        except:
            dummy = ""

test([[1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[30]])
