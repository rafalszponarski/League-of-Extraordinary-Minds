def who_failed(reports, thresholds):
    odp = []
    for uczen, wymog in zip(reports, thresholds):
        imie, wynik = uczen
        if wynik < wymog:
            odp.append(imie)
        
    return odp
    #return [uczen[0] for uczen, wymog in zip(reports, thresholds) if uczen[1] < wymog]