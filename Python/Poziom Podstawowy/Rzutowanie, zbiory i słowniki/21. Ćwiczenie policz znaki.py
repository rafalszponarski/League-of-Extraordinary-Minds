def countChars( s ):
    s = s.upper() #formatowanie tekstu, zignorowac (niezbedne!)
    x = [] #wyjsciowy format, przerobic pozniej an slownik
    y = set() #do porownania (tworzenie x)
    licznik = 0 #numerowanie (druga czesc slownika)
    for i in s:
        if not i in y:
            x.append(i)
        y.add(i)
    odp = dict.fromkeys(x)
    for i in odp:
        for j in s:
            if i == j:
                licznik += 1
        odp[i] = licznik
        licznik = 0

    return odp