def pretty_print(x):
    formatted_x = f"{round(x, 5):^20.5}"
    result = formatted_x.replace(" ", "-")
    print(result)
