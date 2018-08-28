start, stop = [int(x) for x in input("Please enter two numbers: ").split()]

value = start

while value <= stop:
    if value % 2 == 1:
        print(value)

    value += 1
