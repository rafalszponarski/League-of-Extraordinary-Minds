def rgb_dec_code_disp(colors):
    for color in colors:
        name, r, g, b = color
        print(f"{name:<10}|{r:>5}|{g:>5}|{b:>5}")