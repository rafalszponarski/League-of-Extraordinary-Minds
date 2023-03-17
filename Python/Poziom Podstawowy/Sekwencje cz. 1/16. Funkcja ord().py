def maxOrd( text ):
    y=0
    for x in text:
        ord(str(x))
        if ord(str(x)) > y:
            y = ord(str(x))
    return y