def get_percentage( value, text ):
    calosc = int(len(text))
    liczba = text.count(value)
    return liczba/calosc*100
