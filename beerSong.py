

x = 3

while x > 0:
    if x == 1:
        print(x, "bottle of beer on the wall,")
        print(x, "bottle of beer")
    else:
        print(x, "bottles of beer on the wall,")
        print(x, "bottles of beer")

    print("Take one down, pass it around")
    x = x - 1
    if x == 1:
        print(x, "bottle of beer on the wall\n")
    else:
        print(x, "bottles of beer on the wall\n")
