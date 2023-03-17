def dashFormat(password_1, password_2, letter):
    for indeks, litera in enumerate(password_1):
        if litera.lower() == letter or litera.upper() == letter:
            password_2[indeks] = litera

    return password_2