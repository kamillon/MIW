import numpy as np
import math

float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})


def proj(u, v):
    return (np.dot(np.transpose(v), u) / np.dot(np.transpose(u), u)) * u


def dlugoscWektora(v):
    return math.sqrt(np.dot(np.transpose(v), v))


def normalizacja(u):
    return u / dlugoscWektora(u)


def getQ(A):
    v_list = [[x[i] for x in A] for i in range(len(A[1]))]
    Q = []
    u_list = []

    for v in v_list:
        v = np.array(v)
        sum_proj = 0
        for u_x in u_list:
            u_x = np.array(u_x)
            sum_proj += proj(u_x, v)
        u = v - sum_proj
        u_list.append(u)
        if dlugoscWektora(u) == 0:
            e = u
        else:
            e = normalizacja(u)
        Q.append(e)

    return np.array(np.transpose(Q))


def getR(Q, A):
    return np.dot(np.transpose(Q), A)


def getA(Q, R):
    return np.round(np.dot(Q, R))


A = np.array([
    [2, 0],
    [1, 2],
    [0, 1]])

Q = getQ(A)
R = getR(Q, A)
print(Q)
print(R)

print(getA(Q, R))