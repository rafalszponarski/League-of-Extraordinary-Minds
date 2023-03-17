def censor(func, *args, **kwargs):
    pozycyjne = [i for i in args if "k" not in str(i)]
    nazwane = dict((x, y) for x, y in [i for i in kwargs.items() if "k" not in str(i)])

    #print(f"{pozycyjne} \n {nazwane} \n\n")
    
    return func(*pozycyjne, **nazwane)