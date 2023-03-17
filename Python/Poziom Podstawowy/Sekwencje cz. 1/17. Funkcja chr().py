def encrypt( message ):
    y=str('')
    for x in message:
        y += chr( ord(x) * 2 )
        
    return y