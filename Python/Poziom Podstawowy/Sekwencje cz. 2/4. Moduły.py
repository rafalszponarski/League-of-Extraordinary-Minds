import math, balloons

def calcVolume():
    v = 0
    for x in range( balloons.balloonsNumber() ):
        v += 4 / 3 * math.pi * balloons.getRadius( x ) ** 3 / 1000
    return v
