x,y=0,0

def dekorator(func):

    def f(*args, **kwargs):
        x,y=args
        wynik = func(*args, **kwargs)
        print(x,y,x**y)
        return wynik

    return f

@dekorator
def power(x, y):
    return x ** y
    
    
    
    
"""
globalny_licznik = 0

def sledz_funkcje(funkcja):

    def wewnetrzna(*args, **kwargs):
        globalny_licznik += 1
        return funkcja(*args, **kwargs)

    return wewnetrzna
"""