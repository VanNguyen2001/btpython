import math

def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))   
eps = 0.000001
x = 0.5
first = 1
mu = 1
second = 2 * (first * (mu + 2 ) * x**mu / mu)
while (math.fabs(first - second) > eps):
    mu += 2
    first = second
    second = 2 * (first * (mu + 2 ) * x**mu / mu)
print(first)


