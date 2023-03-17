def hasNotAnanym(x):
    wynik = x.copy()
    for a in x:
        for b in x:
            if a == b[::-1]:
                wynik.remove(a)
    return wynik