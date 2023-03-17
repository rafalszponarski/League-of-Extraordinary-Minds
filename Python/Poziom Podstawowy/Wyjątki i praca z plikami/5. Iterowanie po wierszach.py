def avgAge():
    plik = open("data.txt", "r")
    wiek = 0
    wiersze = 0  # licznik
    for i in plik:
        wiek += int(i[0:2])
        wiersze += 1
    return wiek/wiersze
    plik.close()
