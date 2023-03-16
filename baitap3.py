
import math
def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))
x = 1
eps = 0.000001
mu = 1
first = 0
second = - first - x**mu/ mu
while (math.fabs(first - second) > eps):
    mu = mu + 1
    first = second
    second = - first - x**mu / mu
print(first)