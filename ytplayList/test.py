from random import randint

n = 0
while(randint(1,10) != randint(1,10)):
    n = n + 1
    print(n)
    
print("total try:"+str(n))
