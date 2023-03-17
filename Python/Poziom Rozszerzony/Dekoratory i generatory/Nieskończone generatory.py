from itertools import islice


def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


#gen = fibonacci_gen()

#@fibonacci_gen
def nth_fibonacci(n):
    return next(islice(fibonacci_gen(), n, n+1))

