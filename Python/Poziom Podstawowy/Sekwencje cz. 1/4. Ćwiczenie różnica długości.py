#Your code
def diff_len(x, y):
    if len(x) > len(y):
        return len(x)-len(y)
    else:
        return len(y)-len(x)