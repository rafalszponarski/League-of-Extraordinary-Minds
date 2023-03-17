def stringify(obj, human_readable=False):
    return f"Result: {obj!r}" if human_readable == False else f"Result: {obj!s}"