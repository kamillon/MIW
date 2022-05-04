import numpy as np
from math import sqrt

lista = []

with open("punkty.txt", "r") as file:
    for line in file:
        kontekst = line.replace("\n","").split(",")
        lista.append(list(map(lambda e: int(e), kontekst)))


def transpozycja(macierz):
    transposed = []
    for i in range(len(macierz[0])):
        transposed_row = []
        for row in macierz:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed


def regresja(macierz):
    lista_x = []
    lista_y = []
    for i in range(len(macierz)):
        lista_x.append([1, macierz[i][0]])
        lista_y.append(macierz[i][1])

    macierz_x = np.array(lista_x)
    macierz_y = np.array(lista_y)

    # xT = transpozycja(macierz_x)
    xT = np.transpose(macierz_x)
    xTx = np.dot(xT, macierz_x)
    odwrotna = np.linalg.inv(xTx)
    xTy = np.dot(xT, macierz_y)
    return np.dot(odwrotna, xTy)


a = np.array(lista)
print(a)
print(regresja(a))


m1 = np.array([[2,1], [5,2], [7,3], [8,3]])
print(m1)
print(regresja(m1))



