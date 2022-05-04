#sprawdzenie czy w ciągu występuje litera

string1 = "Ala ma kota"
if 'a' in string1:
    print("Tak")


#sprawdzanie czy hasło sprałnia reguły
#musi być dłuża niż 10 znaków
#musi mieć przynajmniej jedną dużą i małą literę oraz !

password = "ZAQ!2wsxqwerty"

def sprawdz(haslo):
    if len(haslo) < 10:
        return False
    if '!' not in haslo:
        return False
    f1 = False
    f2 = False
    for x in haslo:
        if 'A' <= x and x <= 'Z':
            f1 = True
        if 'a' <= x and x <= 'z':
            f2 = True
    return f1 and f2

print(sprawdz(password))


lista = [1, 4, 5, 99, 6]

#funkcja czyNalezy za pomocą pętli while (sprawdza czy liczba należy do listy)
def czyNalezy(elem, lista):
    i = 0
    tmp = False
    while(i < len(lista)):
        for x in lista:
            if elem == lista[i]:
                tmp = True
            i += 1
    return tmp

print(czyNalezy(99,lista))


#wypisanie listy bez elemntu 99
lista2 = [1, 4, 5, 99, 8]

for x in lista:
    if x != 99:
        print(x)


for x in lista:
    if x == 99:
        continue
    print(x)


#odczyt pliku tekstowego i wypisanie go w pętli
file = open("data.txt", "r")
for x in file:
    print(x)

for x in file:
    print(x, end='')