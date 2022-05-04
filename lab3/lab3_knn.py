from math import sqrt

lista = []

with open("australian.dat", "r") as file:
    for line in file:
        kontekst = line.replace("\n", "").split()
        lista.append(list(map(lambda e: float(e), kontekst)))


# print(lista[0:5])
#
# for x in lista[0:5]:
#     print(x)


def metryka_euklidesowa(lista1, lista2):
    tmp = 0
    for i in range(len(lista1) - 1):
        tmp += (lista1[i] - lista2[i]) ** 2
    return sqrt(tmp)


print(metryka_euklidesowa(lista[0], lista[1]))


# def slownikOdleglosci(lista):
#     y = lista[0]
#     slownik = dict()
#     for x in range(1, len(lista)):
#         klasaDecyzyjna = lista[x][-1]
#         if klasaDecyzyjna in slownik:
#             slownik[klasaDecyzyjna].append(metryka_euklidesowa(y, lista[x]))
#         else:
#             slownik[klasaDecyzyjna] = [metryka_euklidesowa(y, lista[x])]
#     return slownik
#
#
# print(slownikOdleglosci(lista))

##################################################

# lista tupli (grupa decyzyjna, odległość)
def odleglosc(x, lista):
    grupy = []
    for i in range(len(lista)):
        decyzyjna = lista[i][-1]
        grupy.append((decyzyjna, metryka_euklidesowa(x, lista[i])))
    return grupy


x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

lista_tuple = odleglosc(x, lista)
print(lista_tuple)


#słownik z kluczem - grupa decyzyjna, wartość - odległość
def grupowanie(lista):
    tmp = {}
    for i in range(len(lista)):
        c = lista[i][0]
        if c not in tmp:
            tmp[c] = []
        tmp[c].append(lista[i][1])
    return tmp


grup = grupowanie(lista_tuple)
print(grup)


#suma k najmniejszych odległości
def sumowanie(grupa, k):
    for key in grupa.keys():
        grupa[key].sort()
    for key in grupa.keys():
        suma = 0
        for i in range(k):
            suma += grupa[key][i]
        grupa[key] = suma
    return grupa


suma2 = sumowanie(grup, 5)
print(suma2)



def decyzja(slownik):
    wynik, min_wartosc = list(slownik.keys())[0], list(slownik.values())[0]
    for key in list(slownik.keys())[1:]:
        if slownik[key] < min_wartosc:
            min_wartosc, wynik = slownik[key], key
        elif slownik[key] == min_wartosc:
            return None
    return wynik


print(decyzja(suma2))
