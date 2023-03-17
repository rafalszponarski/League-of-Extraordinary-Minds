def optimize( operations, toRemove ):
    toRemove.reverse()
    for i in toRemove:
        print(i)
        del(operations[i])
    return operations