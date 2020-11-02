a = 1
b = 1
print("{:>4}".format("  "), end=" ")
for a in range(1, 11):
    print("{:>4}".format(a), end=" ")
print()
for a in range(1, 11):
    print("{:>4}".format(b), end=" ")
    while b <= 10:
        print("{:>4}".format(a*b), end=" ")
        b += 1
    print()
    b = 1