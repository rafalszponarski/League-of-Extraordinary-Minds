def countLucky( numbers ):
    return sum( [num % 7 == 0 for num in numbers] )