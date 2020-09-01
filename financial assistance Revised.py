currentStudent = input("Are you a current student? Yes or No ")
if currentStudent == "Yes":
    gpa = float(input("What is your current GPA? "))
else:
    gpa = 4.0

x = input("Have you ever been convicted of a drug related crime? Yes or No ")

creditHours = int(input("How many credit hours are you going to take? "))
income = float(input("What's your yearly income? "))
if x == "Yes":
    crimeCommitted = True
else:
    crimeCommitted = False
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
