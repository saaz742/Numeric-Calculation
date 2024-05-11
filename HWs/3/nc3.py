import numpy as np
import random


def has_same_dist():
    dis = x[n-1] - x[n-2]
    #print(dis)               wrong float subtract!!
    for i in range(n-2):
        #print(x[i+1]-x[i])
        if(x[i+1]-x[i] != dis):
            return False
    return True

######

def lagrange(x, y, u):
    r = range(len(y))
    a = [y[i]/f(x[i]-x[j]for j in r if j != i)for i in r]
    return sum(a[i]*f([u-x[j] for j in r if j != i]) for i in r)


def f(a):
    p = 1
    for i in a:
        p *= i
    return p

###

def divide(r, x, y, n):
    s = y[0][0]
    for i in range(1, n):
        s += pro(i, r, x) * y[0][i]
    return s


def pro(i, r, x):
    pro = 1
    for j in range(i):
        pro = pro * (r - x[j])
    return pro


def divide_poly(x, y):
    n = x.size
    q = np.zeros((n, n - 1))
    q = np.concatenate((y[:, None], q), axis=1)
    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])
    f = np.zeros(n)
    for i in range(0, n):
        f[i] = q[i, i]

    print("p(x)={:+.4f}".format(f[0]), end="")
    for i in range(1, n):
        print("{:+.4f}".format(f[i]), end="")
        for j in range(1, i + 1):
            print("(x{:+.4f})".format(x[j] * -1), end="")
   

#####

def forward(x, y):
    print("forward: ")
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]
    maxi = max(x)
    mini = min(x)
    r = random.random()
    r = r * (maxi - mini) + mini
    s = y[0][0]
    u = (r - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        s += (cal(u, i) * y[0][i]) / fact(i)
    print("f(" , r, ") =", s)


def backward(x, y):
    print("backward: ")
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1]
    maxi = max(x)
    mini = min(x)
    r = random.random()
    r = r * (maxi - mini) + mini
    s = y[n-1][0]
    u = (r - x[0]) / (x[1] - x[0])
    for i in range(1, n):
        s += (y[n-1][i] * cal(u, i)) / fact(i)
    print("f(" , r, ") = " , s)

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp

##
if __name__ == '__main__':
    x = []
    y = []
    n = int(input())
    x = np.array(input().split(), dtype='float')
    y = np.array(input().split(), dtype='float')
    if(not has_same_dist()): #eshtebah float ra tafrigh mikonad va javabe ghalat midahad!!!!!!
        print("lagrange: \n", lagrange(x, y, 2))
        print("divide: ")
        divide_poly(x, y)
        yn = np.zeros((n, n))
        for i in range(n):
            yn[i][0] = y[i]
        maxi = max(x)
        mini = min(x)
        r = random.random()
        r = r * (maxi - mini) + mini
        print("\nf(" , r, ")= ", divide(r, x, yn, n))
    else:
        yn = np.zeros((n, n))
        for i in range(n):
            yn[i][0] = y[i]
        forward(x, yn)
        backward(x, yn)
