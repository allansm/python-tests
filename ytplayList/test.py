arr1 = [1,1,1,1,1,1,1,1]
arr2 = [2,2,2,2]
arr3 = [3,3,3,3,3,3]
arr4 = [4,4]
mat = [arr1,arr2,arr3,arr4]

def eqMerge(mat):
    big = 0

    for m in mat:
        if(len(m) > big):
            big = len(m)

    print(big)

    arr = []

    for i in range(big):
        for m in mat:
            try:
                arr.append(m[i])
            except:
                error = ""

    return arr

print(eqMerge(mat))
