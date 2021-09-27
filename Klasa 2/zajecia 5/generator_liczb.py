import sys
import random
import getopt
import datetime

def losowanie(min, max, i_liczb, i_losowan):
    wylosowane = []
    try:
        for _ in range(i_losowan):
            liczby = []
            for _ in range(i_liczb):
                liczby.append(random.randint(min, max))
            wylosowane.append(liczby)
    except TypeError:
        print("Program zostal wywolany w nieprawidlowy sposob\nSposob wywolania programu: Generator_liczb_losowych.py -n <zakresmin> -x <zakresmax> -l <liczbaliczb> -p <liczbalosowan> -w <wyswietlanie tak/nie> -z <zapisywanie tak/nie> -p <nazwa_pliku>")
        sys.exit(2)
    return wylosowane

def kontrola(parametr, nazwa):
    if((str(parametr).lower() == 'tak') or (str(parametr).lower() == 'nie')):
        return parametr
    else:
        print("'",nazwa,"' powinno miec wartosc 'tak' lub 'nie'")
        sys.exit(2)

def main(argv):   
    zakres_min = None
    zakres_max = None
    ilosc_liczb = None
    ilosc_losowan = None
    wyswietlanie = None
    zapisywanie = None
    plik_zapisu = None
    try:
        opts, _ = getopt.getopt(argv, "hn:x:l:p:w:z:k:", ["help", "min=", "max=", "liczby=", "proby=", "wyswietlanie=", "zapisywanie=", "plik="])
    except getopt.GetoptError:
        print("Generator_liczb_losowych.py -n <zakresmin> -x <zakresmax> -l <liczbaliczb> -p <liczbalosowan> -w <wyswietlanie tak/nie> -z <zapisywanie tak/nie> -p <nazwa_pliku>")
        sys.exit(2)
    for opt, arg in opts:
        try:
            if opt == '-h':
                print("Generator_liczb_losowych.py -n <zakresmin> -x <zakresmax> -l <liczbaliczb> -p <liczbalosowan> -w <wyswietlanie tak/nie> -z <zapisywanie tak/nie> -p <nazwa_pliku>")
                sys.exit(2)
            elif opt in ("-n", "--min"):
                zakres_min = int(arg)
            elif opt in ("-x", "--max"):
                zakres_max = int(arg)
            elif opt in ("-l", "--liczby"):
                ilosc_liczb = int(arg)
            elif opt in ("-p", "--proby"):
                ilosc_losowan = int(arg)
            elif opt in ("-w", "--wyswietlanie"):
                wyswietlanie = kontrola(arg, "wyswietlanie")
            elif opt in ("-z", "--zapisywanie"):
                zapisywanie = kontrola(arg, "zapisywanie")
            elif opt in ("-k", "--plik"):
                plik_zapisu = arg
        except ValueError:
            print("Program zostal wywolany w nieprawidlowy sposob\nSposob wywolania programu: Generator_liczb_losowych.py -n <zakresmin> -x <zakresmax> -l <liczbaliczb> -p <liczbalosowan> -w <wyswietlanie tak/nie> -z <zapisywanie tak/nie> -p <nazwa_pliku>")
            sys.exit(2)
    wylosowane_liczby = losowanie(zakres_min, zakres_max, ilosc_liczb, ilosc_losowan)
    if(str(wyswietlanie).lower() == 'tak'):
        i = 0
        for _ in wylosowane_liczby:
            print("W losowaniu", i+1, "wylosowano nastepujace liczby:", _)
            i += 1
    if(str(zapisywanie).lower() == 'tak'):
        data = datetime.datetime.now()
        try:
            f = open(plik_zapisu, "a")
            f.write("Losowanie odbylo sie: %s\nIlosc liczb wylosowanych: %s\nIlosc losowan: %s\nZakres liczb: %s-%s\n"%(data,ilosc_liczb,ilosc_losowan,zakres_min,zakres_max))
            i = 0
            for _ in wylosowane_liczby:
                f.write("W losowaniu %s wylosowane nastepujace liczby: %s\n" %(i+1, _))
                i += 1
            f.close
        except IsADirectoryError:
            print("Niewlasciwie podana nazwa pliku zapisu")
            sys.exit(2)
        except:
            print("Wystapil blad przy zapisywaniu do pliku. Sprobuj jeszcze raz")
            sys.exit(2)
            
if _name__=='__main_': main(sys.argv[1:])