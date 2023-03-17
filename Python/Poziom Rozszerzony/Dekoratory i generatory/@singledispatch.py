def count_elements(container):
  # sprawdŸ, jaki typ ma container
  if isinstance(container, list) or isinstance(container, set) or isinstance(container, tuple):
    # dla list, zbiorów i krotek, liczba elementów jest równa d³ugoœci
    return len(container)
  elif isinstance(container, str):
    # dla napisów, liczba elementów jest równa liczbie s³ów
    return len(container.split())
  elif isinstance(container, dict):
    # dla s³owników, liczba elementów jest równa sumie liczby kluczy i wartoœci
    return len(container) + sum(1 for value in container.values())

  # dla innych typów, zwróæ 0
  return 0
