import time
time_start = time.clock()
storeX ={}
def factorial (x):
    if x in storeX:
        return storeX[x]
    elif x == 0:
        return 1
    else:
        xt = x * factorial(x-1)
        storeX[x] = xt
        return xt
print("Factorial of 10 is: ",factorial (10))
print("Computational time is: ",time.clock() - time_start)
