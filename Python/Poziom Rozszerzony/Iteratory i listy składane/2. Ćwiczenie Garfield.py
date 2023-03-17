def countGarfield( names ):
    odp = 1
    letter_iterator = iter(names)
    while True:
        try:
            letter = next(letter_iterator)
            if letter == 'Garfield':
                return odp
            odp += 1
        except StopIteration:
            break

