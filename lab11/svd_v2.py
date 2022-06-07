import numpy as np
import math

def proj(u, v):
    return (np.dot(np.transpose(v), u) / np.dot(np.transpose(u), u)) * u

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

def wartosciWlasne(A):
    A_k = np.copy(A)
    while (isUpperTriangular(A_k) == False):
        Q, R = dekompozycja_QR(A_k)
        A_k = np.dot(np.dot(np.transpose(Q), A_k), Q)
    return np.diag(A_k)

#Funkcja zwraca wartości własne posortowane w odpowiedniej kolejności względem wartości własnych.
#Ponieważ wartości własne zostały posortowane w porządku rosnącym,
#musimy również zmienić kolejność wektorów własnych.
def wektoryWlasne(matrix):
    eigenValues, eigenVectors = np.linalg.eig(matrix)
    idx = eigenValues.argsort()[::-1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]
    return eigenVectors

def SVD(matrix):
    AAT = np.dot(matrix, np.transpose(matrix))
    eigAAT = wektoryWlasne(AAT)
    U = eigAAT
    ATA = np.dot(np.transpose(matrix), matrix)
    eigATA = wektoryWlasne(ATA)
    V = eigATA
    tmp = wartosciWlasne(ATA)
    tmp = np.sort(tmp)[::-1]

    Sigma = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(min(len(Sigma), len(Sigma[0]))):
        Sigma[row][row] = math.sqrt(tmp[row])
    return [np.round(U,decimals=5), np.round(np.array(Sigma),decimals=5), np.round(np.transpose(V),decimals=5)]


A = np.array([[1, 1, 0],
              [0, 1, 2]])

# A = np.array([[1,1,3],
#               [1,2,4],
#               [3,4,6]])

u,sigma,vT = SVD(A)
print("U")
print(u)
print("E")
print(sigma)
print("VT")
print(vT)