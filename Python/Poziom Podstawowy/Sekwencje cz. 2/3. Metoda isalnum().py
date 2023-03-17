def clearText( s ):
    wynik = ''
    for i in s:
        if i.isalnum() == True:
            wynik += i
    return wynik