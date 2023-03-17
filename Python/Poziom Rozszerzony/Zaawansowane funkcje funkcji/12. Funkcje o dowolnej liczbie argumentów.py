def operation(op, *args):
    if op == "+":
        x = 0
        for i in args:
            x += i
        return x
        
    elif op == "*":
        x = 1
        for i in args:
            x *= i
        return x
    