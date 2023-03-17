def bmi( person ):
    _, _, kg, cm = person
    return round(kg/(cm/100)**2, 2)