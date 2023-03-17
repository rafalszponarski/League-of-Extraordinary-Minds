def maxTemp(x):
    max = 0
    for y in x:
        for z in y:
            if z > max:
                max = z
    return max