import math

def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))
eps = 0.0001
x =1
mu = 1
first = 1
second = first + x**mu / factorial(mu)
while (math.fabs(first - second) > eps):
    mu = mu + 1
    first = second
    second = first + x**mu / factorial(mu)
print(first)