def short_list(numbers, k):
  # iteruj po elementach z numbers
  for number in numbers:
    # je¿eli number jest podzielne przez k, zatrzymaj iteracjê
    if number % k == 0:
      break

    # zwróæ number
    yield number
