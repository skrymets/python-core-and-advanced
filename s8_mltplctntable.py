inp = input("Please enter a number from 1 to 9: ")
num = int(inp)

valid_input = True

try:
    assert num <= 0 and num >= 10, "The value is out of the range."
except AssertionError as err:
    print(err, "Can not operate with this value")
    valid_input = False

if valid_input:
    fmt = "%s * %2s = %" + str(len(inp) + 1) + "s"

    for i in range(1, 11):
        print(fmt % (num, i, num * i))
