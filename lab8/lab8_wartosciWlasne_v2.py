import numpy as np
import math

float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind': float_formatter})


def proj(u, v):
    return (np.dot(np.transpose(v), u) / np.dot(np.transpose(u), u)) * u


def norm(v):
    return math.sqrt(np.dot(np.transpose(v), v))


def u_to_e(u):
    return u / norm(u)


def dekompozycja_QR(A):
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
        if norm(u) == 0:
            e = u
        else:
            e = u_to_e(u)
        Q.append(e)

    matrix_q = np.array(np.transpose(Q))
    matrix_r = np.dot(Q, A)
    return matrix_q, matrix_r


def getA(Q, R):
    return np.round(np.dot(Q, R))


def isUpperTriangular(matrix):
    for i in range(1, len(matrix)):
        for j in range(0, i):
            if i == j:
                continue
            elif abs(matrix[i][j]) > 0.0001:
                return False
    return True


def wartosciWlasne(A):
    A_k = np.copy(A)

    while (isUpperTriangular(A_k) == False):
        Q, R = dekompozycja_QR(A_k)
        A_k = np.dot(np.dot(np.transpose(Q), A_k), Q)
    print(A_k)
    print()
    return np.diag(A_k)


# A = np.array([
#     [1, 2, 5],
#     [5, 8, 6],
#     [8, 6, 7]])

A = np.array([
    [3, 2],
    [4, 1]])

Q, R = dekompozycja_QR(A)
print(Q)
print(R)
print("########")

# print(getA(Q,R))

ww = wartosciWlasne(A)
print(ww)