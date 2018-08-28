num = 0


def calc():
    global num
    
    while True:
        inp = input("Please enter a number from 1 to 9: ")
        num = int(inp)
        try:
            assert 0 <= num <= 10, "The value is out of the range."
            break
        except AssertionError as err:
            print(err, "Can not operate with this value")
            continue

    fmt = "%s * %2s = %" + str(len(inp) + 1) + "s"

    for i in range(1, 11):
        print(fmt % (num, i, num * i))


calc()
