def length(sequence, licznik=0):

    if bool(sequence) == True:
        licznik += 1
        _, *sequence = sequence
        return length(sequence, licznik)

    else:
        return licznik