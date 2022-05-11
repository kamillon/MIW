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
        if dlugoscWektora(u) == 0:
            e = u
        else:
            e = normalizacja(u)
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
    wektorWl = np.identity(len(A))

    while (isUpperTriangular(A_k) == False):
        Q, R = dekompozycja_QR(A_k)
        A_k = np.dot(np.dot(np.transpose(Q), A_k), Q)
        wektorWl = np.dot(wektorWl, Q)
    return np.diag(A_k), wektorWl


# A = np.array([
#     [1, 2, 5],
#     [5, 8, 6],
#     [8, 6, 7]])

# A = np.array([
#     [3, 2],
#     [4, 1]])

A = np.array([
    [1, 2, 5],
    [2, 8, 6],
    [5, 6, 7]])

# Q, R = dekompozycja_QR(A)
# print(Q)
# print(R)
# print("########")

# print(getA(Q,R))

# w1, w2 = np.linalg.qr(A)
# print(w1)
# print(w2)

wartoscW, wektorW = np.linalg.eig(A)
print("wartosci wlasne:")
print(wartoscW)
print("wektory wlasne:")
print(wektorW)

print("######################################")
wartoscWlasna, wektorWlasny = wartosciWlasne(A)  #macierz wektorów własnych jest poprawna, gdy macierz A jest symatryczna
print("wartosci wlasne:")
print(wartoscWlasna)
print("-----")
print("wektory wlasne:")
print(wektorWlasny)


# print("wektory wlasne:")
# ww_list = [[round(x[i], 4) for x in wektorWlasny] for i in range(len(wektorWlasny[1]))]
# print(ww_list)