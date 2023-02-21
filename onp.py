stos = []
czyPusty = False
ileObliczen = int(input(""))
if 1 <= ileObliczen <= 1000000:
    while ileObliczen >= 1:
        polecenie = input("")
        if polecenie.lower().startswith("wrzuc"):
            liczba = int(polecenie[-1])
            if -100 <= liczba <= 100:
                stos.append(int(polecenie[-1]))
                ileObliczen -= 1

        if polecenie.lower().startswith("zdejmij"):
            print(stos[-1])
            stos.pop()
            ileObliczen -= 1

        if polecenie.lower().startswith("dodaj"):
            if len(stos) >= 2:
                tmp1 = stos[-1]
                tmp2 = stos[-2]
                stos.pop()
                stos.pop()
                print(tmp1 + tmp2)
                ileObliczen -= 1
            else:
                print("BLAD")
                ileObliczen -= 1

        if polecenie.lower().startswith("odejmij"):
            if len(stos) >= 2:
                tmp1 = stos[-1]
                tmp2 = stos[-2]
                stos.pop()
                stos.pop()
                ileObliczen -= 1
                print(tmp1 - tmp2)
            else:
                print("BLAD")

        licznik = len(stos) - 1
        if polecenie.lower().startswith("wyczysc"):
            while not czyPusty:
                if not stos:
                    czyPusty = True
                    break
                else:
                    czyPusty = False
                print(stos[licznik])
                stos.pop()
                licznik -= 1
            ileObliczen -= 1
    print(stos)
