from faulty_lib import faulty_generator as fgen

with open('wynik.txt', 'w') as file:
    for line in fgen():
        if type(line) == str:
            file.write(line)