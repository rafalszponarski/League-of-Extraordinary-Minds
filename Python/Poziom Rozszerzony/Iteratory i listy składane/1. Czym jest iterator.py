def cleanup(string):
    str = ""
    letter_iterator = iter(string)
    while True:
        try:
            letter = next(letter_iterator)
            if letter.isalnum() == True:
                str += letter
        except StopIteration:
            break

    return str