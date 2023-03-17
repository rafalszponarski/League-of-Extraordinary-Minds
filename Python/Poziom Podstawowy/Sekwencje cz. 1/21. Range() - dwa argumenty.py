def charsInDoc(a, b):
    x = 0
    y=0
    while x <= b:
        y += charsOnPage(a+x)
        x += 1
    return y