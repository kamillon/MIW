def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    #przypadek bazowy dla macierzy 2x2
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for i in range(len(m)):
        determinant += ((-1) ** i) * m[0][i] * getMatrixDeternminant(getMatrixMinor(m, 0, i))
    return determinant


m = [[2, 1, 3, 0],
     [1, 0, 2, 3],
     [3, 2, 0, 1],
     [2, 0, 1, 3]]
d = getMatrixDeternminant(m)
print(d)