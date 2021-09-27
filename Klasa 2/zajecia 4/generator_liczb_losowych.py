import random

zakres_min = 0
zakres_max = 9
ilosc_liczb = 3
ilosc_losowan = 2

def Parametry():
    global zakres_min, zakres_max, ilosc_liczb, ilosc_losowan
    zakres_min = int(input("Podaj liczbe od jakiej chcesz losowac: "))
    zakres_max = int(input("Podaj liczbe do jakiej chcesz losowac: "))
    ilosc_liczb = int(input("Podaj ilosc wygenerowanych liczb w jednym losowaniu: "))
    ilosc_losowan = int(input("Podaj ilosc losowan: "))


def Losowanie(min, max, ilosc, losowanie):
    wylosowane = []
    for _ in range (ilosc):
        wylosowane.append(random.randint(min, max))
    print("W losowaniu ", losowanie+1, " wylosowano nastepujace liczby : ", wylosowane)

while True:
    print("Witaj w generatorze liczb losowych!")
    print("1. Definiowanie parametrow losowania")
    print("2. Wyswietlanie wynikow losowania")
    print("3. Koniec programu")
    decyzja = input()
    if decyzja == '1':
        Parametry()
    elif decyzja == '2':
        i = 0
        while i < ilosc_losowan:
            Losowanie(zakres_min, zakres_max, ilosc_liczb, i)
            i +=1
    elif decyzja == '3':
        exit()
    else:
        print("Wybrales nieprawidlowa opcje. Sprobuj jeszcze raz.")