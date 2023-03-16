import math

def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))
    

eps = 0.001
x = 1
mu = 2
dau = -1
first = 1
second = first + dau * math.pow(x,mu) / factorial(mu)
while (math.fabs(first - second) > eps):
    mu += 2
    dau = -dau
    first = second
    second = first + dau * math.pow(x,mu) / factorial(mu)
print(first)