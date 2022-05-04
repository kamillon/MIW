import numpy as np
from math import sqrt

def srednia(wektor):
    suma = 0
    for i in wektor:
        suma += i
    return suma/len(wektor)


def wariancja(wektor):
    suma = 0
    sr = srednia(wektor)
    for i in wektor:
        suma += (i - sr) ** 2
    return suma/len(wektor)


def odchylenieStandardowe(wektor):
    return sqrt(wariancja(wektor))

######################################################

def srednia2(wektor):
    ones = np.ones(len(wektor))
    wynik = np.dot(ones, wektor)
    return wynik/len(wektor)


def wariancja2(wektor):
    ones = np.ones(len(wektor))
    sr = srednia(wektor)
    a = wektor - sr * ones
    b = np.dot(a, a)
    return b/len(wektor)

def odchylenie2(wektor):
    war = wariancja(wektor)
    return sqrt(war)


tab1 = np.array([4, 6, 2, 4])
tab2 = np.array([5, 5, 5, 5])

# print(srednia2(tab2))
print(wariancja2(tab1))
print(odchylenie2(tab1))