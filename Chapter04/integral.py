import random as rm

rm.seed(3)

f = lambda x: x**2


a = 0.0
b = 3.0


NumSteps = 1000000 
ymin = f(a)
ymax = ymin
for i in range(NumSteps):
    x = a + (b - a) * float(i) / NumSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y

A = (b - a) * (ymax - ymin)
n = 1000000 
R = 0
for j in range(n):
    x = a + (b - a) * rm.random()
    y = ymin + (ymax - ymin) * rm.random()
    if abs(y) <= abs(f(x)):
        if f(x) > 0 and y > 0 and y <= f(x):
            R += 1 
            if f(x) < 0 and y < 0 and y >= f(x):
                R -= 1 

NumIntegral = R / n * A
print ("Numerical integration = " + str(NumIntegral))
