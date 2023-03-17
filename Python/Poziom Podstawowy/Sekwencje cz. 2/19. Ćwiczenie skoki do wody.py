def sumUp(args):
    x = 0
    dlugosc = len(args)//5
    for _ in range(dlugosc):
        zawodnik = args[x : x+5]
        args.insert(x+5, (sum(zawodnik)-max(zawodnik)-min(zawodnik)))
        x += 6
    return args