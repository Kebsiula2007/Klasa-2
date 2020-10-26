"""Program robiący operacje na liście"""

import random
from statistics import median

liczba_elementow=int(input("Ile elementow ma zawierac tablica? "))
list = []

while True:
    decyzja = input("Czy liczby maja byc losowe [tak/nie]? ")
    if decyzja.lower()=="tak":
        najmniejsza = int(input("Podaj najmnniejsza liczbe, ktora moze byc wylosowana: "))
        najwieksza = int(input("Podaj najwieksza liczbe, ktora moze byc wylosowana: "))
        for i in range (liczba_elementow):
            list.append(random.randrange(najmniejsza, najwieksza))
        break
    elif decyzja.lower()=="nie":
        for i in range (liczba_elementow):
            list.append(int(input(f"Wprowadz {i+1} element tablicy: ")))
        break

print(f"Lista: {list}")
print(f"Posortowana lista: {sorted(list)}")
print(f"Lista sklada sie z : {len(list)} elementow")
print(f"Suma elementów listy wynosi: {sum(list)} ")
print(f"Największy element listy ma wartosc: {max(list)} ")
print(f"Najmniejszy element listy ma wartosc: {min(list)} ")
print(f"Średnia wszystkich wartości z listy wynosi: {sum(list)/len(list)}")
print(f"Mediana wszystkich wartośći z listy wynosi: {median(list)} ")