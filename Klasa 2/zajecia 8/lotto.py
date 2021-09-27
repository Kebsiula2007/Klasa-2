from random import randint


class Lotto:
    def __init__(self):
        self.__wylosowane_liczby = []
        self.losowanie()

    def losowanie(self):
        for _ in range(6):
            liczba = randint(1, 49)
            while liczba in self.__wylosowane_liczby:
                liczba = randint(1, 49)
            self.__wylosowane_liczby.append(liczba)

    def pokazywanie(self):
        for _ in sorted(self.__wylosowane_liczby):
            print(_, end=' ')
        print('\n')

    def zapisywanie(self, nazwa_pliku):
        for _ in sorted(self.__wylosowane_liczby):
            nazwa_pliku.write("%s " % (_))
        nazwa_pliku.write('\n')


def wyswietlanie_menu():
    decyzja_menu = 0
    print("\nMenu: ")
    print("1 - Losowanie lotto")
    print("2 - Ilosc losowan (domyslnie jedno)")
    print("3 - Pokazanie losowan")
    print("4 - Zapis do pliku")
    print("5 - Wyjscie z programu")
    decyzja_menu = kontrola_uzytkownika("Wybierz operacje: ", 1, 5)
    return decyzja_menu


def kontrola_uzytkownika(tekst, min_wart, max_wart):
    wart = input(tekst)
    while ((int(min_wart) > int(wart)) or (int(wart) > int(max_wart))):
        print("Wartosc musi byc nie mniejsza niz:", min_wart,
              "i nie wieksza niz:", max_wart, sep=' ')
        wart = input(tekst)
    return int(wart)


print('Generator losowan Lotto')
ilosc_losowan = 1
wylosowane_liczby = []

decyzja_menu = wyswietlanie_menu()
print(decyzja_menu)
while(5 > decyzja_menu):
    if decyzja_menu == 1:
        wylosowane_liczby = []
        for _ in range(ilosc_losowan):
            losowanie = Lotto()
            wylosowane_liczby.append(losowanie)
    elif decyzja_menu == 2:
        ilosc_losowan = kontrola_uzytkownika("Podaj liczbe losowan: ", 0, 100)
    elif decyzja_menu == 3:
        print("Losowania to:")
        for i in range(ilosc_losowan):
            print("W losowaniu", i+1,
                  "wylosowano nastepujace liczby:", sep=' ', end=' ')
            wylosowane_liczby[i].pokazywanie()
    elif decyzja_menu == 4:
        plik_zapisu = open("Losowania_lotto.txt", 'w')
        for _ in range(ilosc_losowan):
            plik_zapisu.write(
                "W losowaniu %s wylosowano nastepujace liczby: " % (_+1))
            wylosowane_liczby[_].zapisywanie(plik_zapisu)
        plik_zapisu.close()
        print("Zapisano do pliku.")
    decyzja_menu = wyswietlanie_menu()