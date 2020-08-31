gpa = float(input("What is your current GPA? "))
x = input("Have you ever been convicted of a drug related crime? ")
if x == "Yes":
    crimeCommitted = True
else:
    crimeCommitted = False
creditHours = int(input("How many credit hours are you going to take? "))
income = float(input("What's your yearly income? "))

if gpa >= 2.0:
    gpa = True
if creditHours >= 6:
    creditHours = True
if income < 50000:
    income = True

if gpa is not True or creditHours is not True or crimeCommitted is True or income is not True:
    print("You are not eligible for financial aid")
else:
    print("You are eligible for financial aid")
