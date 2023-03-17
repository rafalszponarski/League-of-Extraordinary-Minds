#your code
def setAlarm(x, y):
    if x==1 or x==2 or x==3 or x==4 and 22>=y or y>=6:
        return True
    elif x==5 and 18>=y and y>=6:
        return True
    elif x==6 and 14>=y and y>=6:
        return True
    else:
        return False