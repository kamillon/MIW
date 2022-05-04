print("Hello world!")
print("Ala {0} {1}".format("ma", "kota"))

# imie = input("Podaj imie: ")
# print(imie)
# print("Czesc {}".format(imie))
# print(imie[::1])

a = '2'
b = 3
c = 4.2

print("a: {0}, b: {1}, c: {2}".format(type(a), type(b), type(c)))

lista = ["jeden", "dwa", "trzy", "cztery"]
join_list = (" ".join(lista))
print(join_list)

lista2 = join_list.split(' ')
print(lista2)

tekst = "Metody inżynierii wiedzy są najlepsze"
print(tekst)
print('{} ma długosc {}'.format(tekst, len(tekst)))

tekst2 = tekst.replace("ą", "a").replace("ż", "z").replace(" ", "")
print('{} ma długosc {}'.format(tekst2, len(tekst2)))

x = "cos"
y = 2

z = (x, y)
print(z)
print(type(z))

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
wynik = list1 + list2

print(wynik)
print(type(wynik))

print(wynik[3:4])
print(type(wynik[3:4]))

print(list1.index(2))

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

l1.extend(l2)
print(l1)

l1.append(l2)
print(l1)

slownik = {1: "a", 2: "b"}
print(slownik)

krajStolica = {"Polska": "Warszawa", "Niemcy": "Berlin", "Czechy": "Praga", "Litwa": "Wilno", "Ukraina": "Kijów",
            "Rosja": "Moskwa", "Białoruś": "Mińsk", "Słowacja": "Bratysława"}
print(krajStolica)

print(krajStolica.keys())