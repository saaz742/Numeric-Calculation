import numpy as np
from cmath import e
from math import inf, sqrt


def crout(n, matrix):
    l = np.zeros((n, n), dtype=np.double)
    u = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        u[i][i] = 1
        for j in range(i, n):
            tl = float(matrix[j][i])
            for k in range(i):
                tl -= l[j][k]*u[k][i]
            l[j][i] = tl
        for j in range(i+1, n):
            tu = float(matrix[i][j])
            for k in range(i):
                tu -= l[i][k]*u[k][j]
            if int(l[i][i]) == 0:
                l[i][i] = e-40
            u[i][j] = tu/l[i][i]
    return l, u


def doolittle(n, matrix):
    l = np.zeros((n, n), dtype=np.double)
    u = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        for j in range(i, n):
            tu = 0
            for k in range(i):
                tu += l[i, k]*u[k, j]
            u[i, j] = matrix[i, j] - tu
        for j in range(i, n):
            if i == j:
                l[i, i] = 1
            else:
                tl = 0
                for k in range(i):
                    tl += l[j, k]*u[k, i]
                l[j, i] = (matrix[j, i] - tl)/u[i, i]
        return l, u


def cholesky(n, matrix):
    l = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        for j in range(i + 1):
            tl = 0
            if j == i:
                for k in range(j):
                    tl += pow(l[j][k], 2)
                if matrix[j][j] - tl >= 0:
                    l[j][j] = int(sqrt(matrix[j][j] - tl))
                else:
                    return "no l", "no u"
            else:
                for k in range(j):
                    tl += (l[i][k] * l[j][k])
                if l[j][j] > 0:
                    l[i][j] = int((matrix[i][j] - tl) / l[j][j])
    return l, "no u"


if __name__ == '__main__':
    matrix = []
    n = int(input())
    for i in range(n):
        matrix.append(list(map(int,  input().replace(",", "").split())))
        # if there is no , in input use line below
        #matrix.append(list(map(int,  input().split())))
    name = input().lower()
    if name == "crout":
        l, u = crout(n, np.array(matrix))
    elif name == "doolittle":
        l, u = doolittle(n, np.array(matrix))
    elif name == "cholesky":
        l, u = cholesky(n, np.array(matrix))

    print("L: \n", l, "\n ----------------------------------- ")
    print("U: \n", u)
