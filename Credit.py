
creditScore = int(input("What's your credit score? "))


if 300 <= creditScore <= 629:
    print("You have bad credit")
elif 630 <= creditScore <= 689:
    print("You have fair credit")
elif 690 <= creditScore <= 719:
    print("You have good credit")
elif 720 <= creditScore <= 850:
    print("You have excellent credit")
else:
    print("You have entered an invalid credit score")
