def count_elements(container):
  # sprawd�, jaki typ ma container
  if isinstance(container, list) or isinstance(container, set) or isinstance(container, tuple):
    # dla list, zbior�w i krotek, liczba element�w jest r�wna d�ugo�ci
    return len(container)
  elif isinstance(container, str):
    # dla napis�w, liczba element�w jest r�wna liczbie s��w
    return len(container.split())
  elif isinstance(container, dict):
    # dla s�ownik�w, liczba element�w jest r�wna sumie liczby kluczy i warto�ci
    return len(container) + sum(1 for value in container.values())

  # dla innych typ�w, zwr�� 0
  return 0
