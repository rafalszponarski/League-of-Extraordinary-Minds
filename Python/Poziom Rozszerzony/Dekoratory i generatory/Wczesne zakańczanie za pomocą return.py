def short_list(numbers, k):
  # iteruj po elementach z numbers
  for number in numbers:
    # je�eli number jest podzielne przez k, zatrzymaj iteracj�
    if number % k == 0:
      break

    # zwr�� number
    yield number
