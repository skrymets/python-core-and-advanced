def display(data):
    print("Hello, ", data(), "!", sep="")


def name():
    return "World"


display(name)
