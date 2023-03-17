def isPalindrom(x):
    y = x.copy()
    y.reverse()
    if y == x:
        return True
    else:
        return False