def valueToDecimal(value, base):
    #return int(value, base)
    odp = 0
    for indeks, liczba in enumerate(value[::-1]):
        odp += int(liczba) * base**indeks
    
    return odp