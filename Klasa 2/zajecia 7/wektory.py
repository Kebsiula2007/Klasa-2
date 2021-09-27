from math import pi, cos, sin


class Wektor:
    ilosc_wektorow = 0

    @staticmethod
    def odleglosc(w1, w2):
        return ((w1.y-w2.y)**2 + (w2.x-w1.x)**2)**0.5

    @classmethod
    def tworzenie_cartesians(cls, nazwa='No name', x=0, y=0):
        return cls(nazwa, x, y)

    @classmethod
    def tworzenie_polar(cls, nazwa='No name', r=0, thetha=0):
        return cls(nazwa, r*cos(thetha), r*sin(thetha))

    def __init__(self, nazwa="No name", x=0, y=0):
        self.poczatek_x, self.poczatek_y = 0, 0
        self.x, self.y = x, y
        self.nazwa = nazwa
        Wektor.ilosc_wektorow += 1
        print(
            f'Wektor {self.nazwa} o końcu w ({self.x}, {self.y}) został utworzony')

    def __del__(self):
        Wektor.ilosc_wektorow -= 1
        print(
            f'Wektor {self.nazwa} o końcu w ({self.x}, {self.y}) został zniszczony')

    def dlugosc(self) -> float:
        return (self.x**2+self.y**2)**0.5

    def skalowanie(self, czynnik):
        self.x, self.y = self.x*czynnik, self.y*czynnik
        return f'Nowe wspolrzedne {self.nazwa} ({self.x}, {self.y})'

    def __str__(self):
        return f'Wektor {self.nazwa} o końcu w ({self.x}, {self.y})'


def funkcja():
    print(f'Ilość wektorów: {Wektor.ilosc_wektorow}')
    wektor2 = Wektor('W2', 7, 7)
    wektor3 = Wektor.tworzenie_polar('W3', 5, pi/6)
    print(wektor1)
    print(
        f'Odległość między końcami wektorów {wektor1.nazwa} i {wektor2.nazwa}: {Wektor.odleglosc(wektor1, wektor2)}')
    print(f'Ilość wektorów: {Wektor.ilosc_wektorow}')


wektor1 = Wektor('W1', 4, 3)
funkcja()
wektor4 = Wektor.tworzenie_cartesians('W4', 3, 2)
print(wektor4.skalowanie(2))
print(f'Ilość wektorów: {Wektor.ilosc_wektorow}')
print(f'Długość wektora {wektor1.nazwa}: {wektor1.dlugosc()}')