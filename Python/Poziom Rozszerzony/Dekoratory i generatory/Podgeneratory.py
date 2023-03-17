def join_with(iterators, sep):
  # je�eli lista iterators jest pusta, zwr�� pusty iterator
  if not iterators:
    return

  # zmienna first_iter przechowuje informacj�, czy jest to pierwszy iterator z listy
  first_iter = True

  # iteruj po iteratorach z listy iterators
  for iterator in iterators:
    # je�eli jest to pierwszy iterator, nie wypisuj element�w z sep
    if first_iter:
      first_iter = False
    # w przeciwnym wypadku, wypisuj elementy z sep
    else:
      for item in sep:
        yield item

    # wypisuj elementy iteratora
    for item in iterator:
      yield item
