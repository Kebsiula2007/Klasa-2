from abc import ABC, abstractmethod

figury = []


class Figura(ABC):
    def __init__(self):
        self.pole = 0
        self.obwod = 0

    def zapisywanie(self):
        figury.append(self.__dict__)

    @abstractmethod
    def liczenie_pola(self):
        pass

    def liczenie_obwodu(self):
        pass


class Prostokat(Figura):
    def __init__(self, nazwa="No name", a=0, b=0):
        self.figura = "Prostokat"
        self.nazwa = nazwa
        self.a = a
        self.b = b
        super().__init__()
        self.liczenie_pola()
        self.liczenie_obwodu()
        super().zapisywanie()

    def liczenie_pola(self):
        self.pole = self.a * self.b

    def liczenie_obwodu(self):
        self.obwod = (self.a+self.b)*2


class Kwadrat(Figura):
    def __init__(self, nazwa="No name", a=0):
        self.figura = "Kwadrat"
        self.nazwa = nazwa
        self.a = a
        super().__init__()
        self.liczenie_pola()
        self.liczenie_obwodu()
        super().zapisywanie()

    def liczenie_pola(self):
        self.pole = self.a ** 2

    def liczenie_obwodu(self):
        self.obwod = 4 * self.a


class Trojkat(Figura):
    def __init__(self, nazwa="No name", a=0, b=0, c=0, h=0):
        self.figura = "Trojkat"
        self.nazwa = nazwa
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        super().__init__()
        self.liczenie_pola()
        self.liczenie_obwodu()
        super().zapisywanie()

    def liczenie_pola(self):
        self.pole = (self.a * self.h)/2

    def liczenie_obwodu(self):
        self.obwod = self.a + self.b + self.c


class Romb(Figura):
    def __init__(self, nazwa="No name", a=0, h=0):
        self.figura = "Romb"
        self.nazwa = nazwa
        self.a = a
        self.h = h
        super().__init__()
        self.liczenie_pola()
        self.liczenie_obwodu()
        super().zapisywanie()

    def liczenie_pola(self):
        self.pole = self.a * self.h

    def liczenie_obwodu(self):
        self.obwod = 4 * self.a


prostokat1 = Prostokat("P1", 3, 4)
kwadrat1 = Kwadrat("K1", 6)
trojka1 = Trojkat("T1", 4, 3, 5, 5)
romb1 = Romb("R1", 10, 20)
kwadrat2 = Kwadrat("K2", 10)
prostokat2 = Prostokat("P2", 6, 8)
print(figury)