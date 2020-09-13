
currentAge = int(input("What is your age? "))
retireAge = int(input("At what age do you want to retire? "))
currentIncome = int(input("What is your current income? "))
percentSaved = int(input("What percentage of your income do you save? "))
alreadySaved = int(input("How much do you have in savings currently? "))
contribution = currentIncome * (percentSaved/100)
print(format("Age", "5") + format("Income", "15") + format("Contribution", "22") + format("Total", "5"))

print(currentAge, format(currentIncome, "8") + format(int(contribution), "20") + format(alreadySaved, "17"))

for x in range(currentAge, retireAge + 1):
    currentIncome = currentIncome * 1.03
    contribution = currentIncome * percentSaved/100
    alreadySaved = alreadySaved * 1.06
    alreadySaved = contribution + alreadySaved

    print(x, format(int(currentIncome), "8") + format(int(contribution), "20") + format(int(alreadySaved), "17"))
