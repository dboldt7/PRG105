
income = float(input("How much do you make in a month? "))
housing = float(input("How much do you spend on housing per month? "))
food = float(input("How much do you spend on food per month? "))
transportation = float(input("How much do you spend on transportation per month? "))
phone = float(input("How much is your phone bill per month? "))
utilities = float(input("How much is your utility bill per month? "))
clothing = float(input("How much do spend on clothing per month? "))

totalExpenses = housing + food + transportation + phone + utilities + clothing
moneyLeft = income - totalExpenses

if moneyLeft < 0:
    print("You're in debt!")
else:
    print("  ")
    print("Housing makes up ", format(housing/totalExpenses, '.2%'), " of your expenses")
    print("Food makes up ", format(food/totalExpenses, '.2%'), " of your expenses")
    print("Transportation makes up ", format(transportation/totalExpenses, '.2%'), " of your expenses")
    print("Your phone bill makes up ", format(phone/totalExpenses, '.2%'), " of your expenses")
    print("Your utility bill makes up ", format(utilities/totalExpenses, '.2%'), " of your expenses")
    print("Clothing makes up ", format(clothing/totalExpenses, '.2%'), " of your expenses")
    print("You have $", moneyLeft, " left to spend!")
