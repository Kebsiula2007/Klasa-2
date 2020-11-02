"""Program szukajacy miejsc zerowych funkcji liniowej"""

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
if a != 0:
    x = -b/a
    print("Miejsce zerowe funkcji liniowej wynosi: ", x)
elif a == 0 and b == 0:
    print("Funkcja liniowa ma nieskonczenie wiele miejsc zerowych")
else:
    print("Funkcja liniowa nie ma miejsca zerowego")
