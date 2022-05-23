import numpy as np
import math

BT = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, -1, -1, -1, -1],
               [1, 1, -1, -1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, -1, -1],
               [1, -1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, -1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, -1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, -1]])

XA = np.array([8, 6, 2, 3, 4, 6, 6, 5])  # XA jest transponowane


def czyDiagonalna(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if ((i != j) and (matrix[i][j] != 0)):
                return False
    return True


def normalizacjaMacierzy(matrix):
    M = []
    for v in matrix:
        M.append(v / math.sqrt(np.dot(np.transpose(v), v)))
    return np.array(M)


s = np.dot(BT, np.transpose(BT))
macierzOrtonormalna = normalizacjaMacierzy(BT)
XB = np.dot(macierzOrtonormalna, XA)

# print(czyDiagonalna(s))
# print(macierzOrtonormalna)
print(XB)
