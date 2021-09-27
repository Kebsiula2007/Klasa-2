import random

class losowanie():
    def __init__(self):
        self.zgadywana_liczba = random.randint(0,100)
        self.szukanie()

    def szukanie(self):
        self.podana_liczba = int(input("Podaj liczbe:"))
        self.mniejwiecej()
    def mniejwiecej(self):
        if self.zgadywana_liczba < self.podana_liczba:
            print("Podana liczba jest za duza. Probuj dalej:")
        elif self.zgadywana_liczba > self.podana_liczba:
            print("Podana liczba jest za mała. Probuj dalej:")
        else:
            print("luhuuu ogadłes liczbe!!!")

        self.szukanie()

    losowanie1 = losowanie()
    losowanie1.szukanie()