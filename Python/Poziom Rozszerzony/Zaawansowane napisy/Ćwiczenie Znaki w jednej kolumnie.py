def pretty_print(numbers):
    for number in numbers:
        sign = "+" if number >= 0 else "-"
        number_str = "{:>{width}}".format(abs(number), width=9)
        print(f"{sign}{number_str}")