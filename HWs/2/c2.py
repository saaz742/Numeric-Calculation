# ax^3 + bx^2 + cx + d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
x0 = int(input())

poly = [a,b,c,d]

#poly[0]x(n-1) + poly[1]x(n-2) + .. + poly[n-1]
def horner(poly, x):
    res = poly[0] 
    for i in range(1, 4):
        res = poly[i] + res*x 
    return res
  
print("Value: " , horner(poly, x0))