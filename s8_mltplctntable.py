inp = input("Please enter a number from 1 to 9: ")
num = int(inp)

fmt = "%s * %2s = %" + str(len(inp) + 1) + "s"

for i in range(1, 11):
    print(fmt % (num, i, num * i))
