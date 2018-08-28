info = ("id", "name", "scores")
profile = {}
handlers = {"id": lambda x: x,
            "name": lambda x: x,
            "scores": lambda x: [float(v) for v in x.split()]
}

for key in info:
    val = input("Enter student's %s: " % (key,))
    profile[key] = handlers[key](val)

print(profile)
