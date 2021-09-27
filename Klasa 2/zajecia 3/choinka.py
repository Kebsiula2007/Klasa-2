print("Program rysuje choinke z *\n")
a = 6
b = 3
for c in range(b):
    x = a - 1
    f = x
    z = 1
    for d in range(a):
        print(" " * x + "*" * z + " " * x)
        z += 2
        x -= 1
for e in range(b):
    print(" " * f + "*" + " " * f)