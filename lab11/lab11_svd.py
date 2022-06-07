import numpy as np
import math

def identity(rows, cols):
    eye = [[] for j in range(rows)]
    index = 0
    for row in eye:
        for i in range(cols):
            if i == index:
                row.append(1)
            else:
                row.append(0)
        index += 1
    return eye


def proj(u, v):
    tmp1 = np.dot(np.transpose(v), u)
    tmp2 = np.dot(np.transpose(u), u)
    if(tmp2 == 0):
        return 0
    return tmp1 / tmp2 * u


def dlugoscWektora(v):
    return math.sqrt(np.dot(np.transpose(v), v))


def normalizacja(u):
    return u / dlugoscWektora(u)


def dekompozycja_QR(A):
    lista_v = [[x[i] for x in A] for i in range(len(A[0]))]
    Q = []
    lista_u = []
    for v in lista_v:
        v = np.array(v)
        suma_projekcji = 0
        for x in lista_u:
            x = np.array(x)
            suma_projekcji += proj(x, v)
        u = v - suma_projekcji
        lista_u.append(u)
        if dlugoscWektora(u) == 0:
            e = u
        else:
            e = normalizacja(u)
        Q.append(e)

    matrix_q = np.array(np.transpose(Q))
    matrix_r = np.dot(Q, A)
    return matrix_q, matrix_r


def isUpperTriangular(matrix):
    for i in range(1, len(matrix)):
        for j in range(0, i):
            if i == j:
                continue
            elif abs(matrix[i][j]) > 0.0001:
                return False
    return True


def eig(matrix):
    wektorWl = identity(len(matrix), len(matrix[0]))
    A_k = matrix.copy()

    while (isUpperTriangular(A_k) == False):
        Q, R = dekompozycja_QR(A_k)
        wektorWl = np.dot(wektorWl, Q)
        R = np.dot(np.linalg.pinv(Q), A_k)
        A_k = np.dot(R, Q)
    return A_k, wektorWl


def SVD(matrix):
    AAT = np.dot(matrix, np.transpose(matrix))
    eigAAT = eig(AAT)
    U = eigAAT[1]
    ATA = np.dot(np.transpose(matrix), matrix)
    eigATA = eig(ATA)
    V = eigATA[1]
    tmp = eigATA[0]
    Sigma = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(min(len(Sigma), len(Sigma[0]))):
        Sigma[row][row] = math.sqrt(tmp[row][row])
    return [U, np.array(Sigma), np.transpose(V)]



A = np.array([[1, 1, 0],
              [0, 1, 2]])


u,sigma,vT = SVD(A)
print("U")
print(u)
print("E")
print(sigma)
print("VT")
print(vT)
print()

matrixA = np.round(np.dot(np.dot(u,sigma),vT))
print("A")
print(matrixA)