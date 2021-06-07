from tkinter import *

root = Tk()
root.title("Kalkulator")

liczba1 = Entry(root, width=30, borderwidth=10)
liczba1.grid(row=0, column=0, columnspan=4, rowspan=3)
liczba2 = Entry(root, width=30, borderwidth=10)
liczba2.grid(row=4, column=0, columnspan=4, rowspan=3)

dzialanie = IntVar()
dzialanie.set("2")

Radiobutton(root, text="+", variable=dzialanie, value=43).grid(row=3, column=0)
Radiobutton(root, text="-", variable=dzialanie, value=45).grid(row=3, column=1)
Radiobutton(root, text="*", variable=dzialanie, value=42).grid(row=3, column=2)
Radiobutton(root, text="/ ", variable=dzialanie,
            value=47).grid(row=3, column=3)

dekoracja1 = Label(root, text="-------------------------------")
dekoracja1.grid(row=2, column=4, columnspan=3, sticky=N)
dekoracja2 = Label(root, text="-------------------------------")
dekoracja2.grid(row=4, column=4, columnspan=3, sticky=S)
dekoracja3 = Label(root, text="|\n|\n|\n")
dekoracja3.grid(row=2, column=7)
dekoracja4 = Label(root, text="|\n|\n|\n")
dekoracja4.grid(row=4, column=7)


def clicked(znak):
    wynik = None
    try:
        a = int(liczba1.get())
        b = int((liczba2.get()))
    except TypeError and ValueError:
        exit("Nie podales liczby!")
    else:
        if b == 0 and znak == '/':
            myLabel = Label(root, text="Nie można dzielić przez zero!!!")
        else:
            if znak == '+':
                wynik = a+b
            elif znak == '-':
                wynik = a-b
            elif znak == '*':
                wynik = a*b
            elif znak == '/':
                wynik = a/b
            myLabel = Label(root, text="%s %s %s = %s" % (a, znak, b, wynik))
        myLabel.grid(row=3, column=6, columnspan=2)


mojPrzycisk = Button(root, text="Oblicz!",
                     command=lambda: clicked(chr(dzialanie.get())))
mojPrzycisk.grid(columnspan=4)

root.mainloop()