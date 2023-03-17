def findGreater( oil, value ):
    odp = []
    for i, el in enumerate(oil):
        if el >= value:
            odp.append(i)
    
    return odp