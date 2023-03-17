def convert( x ):
    wynik = x.copy()
    for i in wynik:
        if i > 10:
            wynik[wynik.index(i)] = 10
        elif i < 0:
            wynik[wynik.index(i)] = 0
        else:
            wynik[wynik.index(i)] = i
    
    return (x+wynik)