def getEmails( s1, s2 ):
    
    final = set()
    s3 = s1+s2
    for i in s3:
        if i[1] == True:
            final.add(i[0])
            
    return final