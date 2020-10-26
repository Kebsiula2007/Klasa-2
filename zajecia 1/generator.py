import random
print("program losuje liczbe od 0 do 100, a gracz ma zadanie ją zgadnąć")
wylosowana_liczba = random.randrange(1, 100)
wpisana_liczba = 0
liczba_prob = 0
while wpisana_liczba != wylosowana_liczba:
    wpisana_liczba = int(input("Wpisz liczbę: "))
    liczba_prob += 1
    if wpisana_liczba > wylosowana_liczba:
        print("Podałeś za dużą liczbę")
    elif wpisana_liczba < wylosowana_liczba:
        print("Podałeś za małą liczbę")
    else:
        print("Brawo, zgadłeś za", liczba_prob, "razem!")