#your code
def checkTriangle(x, y, z):
    if x>y and x>z and x<y+z:
            return True
    elif y>x and y>z and y<z+x:
            return True
    elif z>y and z>x and z<y+x:
            return True
    else:
        return False