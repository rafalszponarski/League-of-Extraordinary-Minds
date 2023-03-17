def bestStudent( studentScores ):
    return sorted(studentScores, key=lambda m: m[1], reverse=True)[0][0]