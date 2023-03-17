def encrypt(message):
    x=0
    z=''
    for y in message:
        y = str(chr(int(ord(str(y)))+int(x)))
        z += y
        x += 1
    return z