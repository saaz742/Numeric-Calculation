#ln(n) = (n-1) - (n-1)^2/2 + (n-1)^3/3 +...+ (-1)^(i+1)*(n-1)^i/i
#ln(n) = lim i(n^(i-1)-1) i to infinity
import math

def ln(n):
    x = 10000.0
    return x*((n**(1/x))-1)

def roundDown(x, decimal = 0):
    mul = 10 ** decimal
    return math.floor(x * mul) / mul

n = float(input())
l = ln(n)
absoluteError = abs(l-roundDown(l,4))
relativeError = absoluteError/l
print('actual:',l)
print('absolute:', absoluteError)
print('relative:', relativeError)
# 4 ragham ashar gerd konad
print('absolute:', round(absoluteError,4))
print('relative:', round(relativeError,4))
