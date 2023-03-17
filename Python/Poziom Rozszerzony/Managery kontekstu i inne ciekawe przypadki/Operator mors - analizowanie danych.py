from dataDispenser import nextValue

def analyze(size):
    values = (nextValue() for _ in range(size))
    filtered_values = filter(lambda x: x > 3.14, values)
    return sum(filtered_values)
