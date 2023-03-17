def weightedRating( rating, weight ):
    return [round(ocena*waga, 1) for ocena, waga in zip(rating, weight)]
