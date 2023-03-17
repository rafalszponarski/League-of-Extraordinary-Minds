def decrypt( message, key):
    y=str('')
    for x in message:
        y += chr( int(ord(x)) // int(key) )
        
    return y