
creditScore = int(input("What's your credit score? "))


if creditScore <= 629:
    print("You have bad credit")
elif creditScore <= 689:
    print("You have fair credit")
elif creditScore <= 719:
    print("You have good credit")
else:
    print("You have excellent credit")
