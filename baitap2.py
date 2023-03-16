
import math

def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))
x = 0.5
eps = 0.000001
mu = 1
dau = -1
first = 1
second = first + dau * ((mu+1) * (mu+2) / 2) * x**mu
while (math.fabs(first - second) > eps):
    mu = mu +1
    dau = - dau
    first = second
    second = first + dau * ((mu+1) * (mu+2) / 2) * x**mu
print(first)