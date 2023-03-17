def first_powers(k):
  # zmienna power przechowuje obecn¹ potêgê dwójki
  power = 1

  # zwracamy generator z wyra¿eniem generatora
  return (power * 2 ** i for i in range(k))
