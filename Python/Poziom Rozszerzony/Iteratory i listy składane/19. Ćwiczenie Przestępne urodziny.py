def czyPrzestepny(rok):
    return (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0)
    
def leapUsers( users ):
    licznik = 0

    for i in users:
        if czyPrzestepny(int(i[:4])):
            licznik += 1
            
    return licznik