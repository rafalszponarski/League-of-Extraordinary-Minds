def monthReport( data ):
    odp = []
    for indeks, testy in enumerate(data):
        liczba, pozytywne = testy
        if pozytywne > liczba/2:
            odp.append(indeks+1)
            
    return odp