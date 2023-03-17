def switchType(arg):
    if isinstance(arg, (int, float)):
        return str(arg)
    elif isinstance(arg, str):
        try:
            return int(arg)
        except ValueError:
            return float(arg)
    else:
        raise TypeError("Argument must be int, float, or str")
