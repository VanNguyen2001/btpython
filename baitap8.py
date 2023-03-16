import math

def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))

def tichChan(n):
    rs = 1
    for i in range(1, n + 1) :
        if(i%2 == 0):
            rs = rs * i
    return rs
def tichLe(n):
    rs = 1
    for i in range(1, n + 1) :
        if(i%2 != 0):
            rs = rs * i
    return rs


eps = 0.001
x = 1
mu = 3
first = x
second = first + tichLe(mu - 1) / tichChan(mu - 1) * x**mu / mu
while(math.fabs(first - second) > eps):
    mu += 2 
    first = second
    second = first + tichLe(mu - 1) / tichChan(mu - 1) * x**mu / mu
print(first)