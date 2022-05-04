from math import sqrt
import numpy as np
import random

lista = []

with open("australian.dat", "r") as file:
    for line in file:
        kontekst = line.replace("\n","").split()
        lista.append(list(map(lambda e: float(e), kontekst)))


def metryka_euklidesowa2(lista1, lista2):
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    c = v1 - v2
    wynik = sqrt(np.dot(c, c))
    return wynik



def listaBezKlasy(lista):
    bezKlasy = []
    for x in lista:
        bezKlasy.append(x[:-1])
    return bezKlasy

list_without_class = listaBezKlasy(lista)
print(list_without_class)


def randomowaKlasaDecyzyjna(lista, k):
    for x in lista:
        r = random.randint(0, k-1)
        x.append(float(r))
    return lista

list_random = randomowaKlasaDecyzyjna(list_without_class, 2)
print(list_random)


def toDict(lista, tmp):
    slownik = dict()
    for x in range(len(lista)):
        klasaDecyzyjna = lista[x][-1]
        if klasaDecyzyjna not in slownik:
            slownik[klasaDecyzyjna] = []
        slownik[klasaDecyzyjna].append(tmp[x])
    return slownik


def kMeans(lista):
    suma = 0
    tmp = []
    for i in range(7):
        for i in range(len(lista)):
            for j in range(len(lista)):
                if lista[i][-1] == lista[j][-1]:
                    suma += metryka_euklidesowa2(lista[i], lista[j])
            tmp.append(suma)
            suma = 0
        d = toDict(lista, tmp)
        d3 = []
        for x in d.keys():
            decyzyjna = x
            d3.append((decyzyjna, min(d[x]), tmp.index(min(d[x]))))

        for i in range(len(lista)):
            for j in range(1, len(d3)):
                min2 = metryka_euklidesowa2(lista[i], lista[d3[0][2]])
                metryka = metryka_euklidesowa2(lista[i], lista[d3[j][2]])
                if min2 >= metryka:
                    min2 = metryka
                    if lista[i][-1] != d3[j][0]:
                        lista[i][-1] = d3[j][0]
                else:
                    lista[i][-1] = d3[0][0]
    return lista


# random_class = [[1.0, 16.0, 14.0, 0.0], [1.0, 3.0, 12.0, 2.0], [1.0, 2.0, 11.0, 2.0], [3.0, 9.0, 18.0, 1.0], [2.0, 8.0, 6.0, 0.0], [10.0, 2.0, 25.0, 1.0]]
# random_class2 = [[1.0, 16.0, 14.0, 0.0], [1.0, 3.0, 12.0, 2.0], [1.0, 2.0, 11.0, 2.0], [3.0, 9.0, 18.0, 1.0], [2.0, 8.0, 6.0, 0.0], [10.0, 2.0, 25.0, 1.0]]

lista_sm = kMeans(list_random)
# lista_sm = kMeans(random_class)
print(lista_sm)


def klasaIlosc(lista):
    slownik = dict()
    for x in range(len(lista)):
        klasaDecyzyjna = lista[x][-1]
        if klasaDecyzyjna in slownik:
            slownik[klasaDecyzyjna] += 1
        else:
            slownik[klasaDecyzyjna] = 1
    return slownik

ilosc = klasaIlosc(lista_sm)

for k, v in ilosc.items():
    print("klasa decyzyjna {}: {}".format(k, v))


def stosunekPokrycia(lista1, lista2):
    ile = 0
    for i in range(len(lista1)):
        if(lista1[i] == lista2[i]):
            ile += 1
    return str((ile)/len(lista1)*100)+" % pokrycia w stosunku do listy wejściowej"

print(stosunekPokrycia(lista, lista_sm))