import math
from matplotlib import pyplot as plt


def func(x, s):
    return (x**s)*math.exp(x)


def simpson3_8(a, b, n, s):
    h = (b-a)/n
    sum = func(a, s) + func(b, s)
    for i in range(1, n):
        if (i % 3 == 0):
            sum += 2 * func(a + i * h, s)
        else:
            sum += 3 * func(a + i * h, s)
    return ((float(3 * h) / 8) * sum)


def simpsons1_3(a, b, n, s):
    h = (b-a)/n
    x = list()
    f = list()
    for i in range(n):
        x.append(a + i * h)
        f.append(func(x[i], s))
    sum = 0
    for i in range(n):
        if i == 0 or i == n:
            sum += f[i]
        elif i % 2 != 0:
            sum += 4 * f[i]
        else:
            sum += 2 * f[i]
    sum *= h / 3
    return sum


def trapezoidal(a, b, n, s):
    h = (b - a) / n
    sum = func(a, s) + func(b, s)
    for i in range(1, n):
        k = a + i*h
        sum += 2 * func(k, s)
    sum *= h/2
    return sum


def Rectangle(a, b, n, s):
    h = (b-a)/n
    sum = 0
    for i in range(n):
        x = a + i*h
        sum += h * func(x, s)
    return sum


if __name__ == '__main__':
    n = int(input())
    a = int(input())  # lower
    b = int(input())  # upper
    s = int(input())
    print("simpson 3/8: ", simpson3_8(a, b, n, s))
    print("simpson 1/3: ", simpsons1_3(a, b, n, s))
    #print("rectangle: ", Rectangle(a, b, n, s))
    print("trapezoidal: ", trapezoidal(a, b, n, s))
    n = 0
    simp3_8 = list()
    simp1_3 = list()
   # rect = list()
    trapezoida = list()
    for n in range(1, 100):
        simp3_8.append(simpson3_8(a, b, n, s))
        simp1_3.append(simpsons1_3(a, b, n, s))
       # rect.append(Rectangle(a, b, n, s))
        trapezoida.append(Rectangle(a, b, n, s))
    plt.plot(simp3_8)
    plt.plot(simp1_3)
    #plt.plot(rect)
    plt.plot(trapezoida)
    plt.show()
