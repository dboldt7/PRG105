occupation = None
specialDiscount = input("Are you a sponsor, student, retiree, or veteran? Yes or No ")
if specialDiscount == "Yes":
    occupation = input("Which category do you belong to? ").lower()
ticketNumber = int(input("How many tickets are you purchasing? "))
ticketPrice = None
ticketDiscount = None
initialPrice = None
finalPrice = None

if occupation == "sponsor":
    ticketPrice = 2.00
elif occupation == "student":
    ticketPrice = 5.00
elif occupation == "retiree":
    ticketPrice = 6.00
elif occupation == "veteran":
    ticketPrice = 7.00
else:
    ticketPrice = 10.00

if ticketNumber > 15:
    ticketDiscount = 0.2
elif ticketNumber >= 9:
    ticketDiscount = 0.15
elif ticketNumber >= 4:
    ticketDiscount = 0.10
else:
    ticketDiscount = 0

initialPrice = ticketNumber * ticketPrice
print("Your cost before the discount is $", format(initialPrice, ".2f"))
finalPrice = initialPrice - (initialPrice * ticketDiscount)
print("Your cost after the discount is $", format(finalPrice, ".2f"))
print("Your price per ticket is $", format(finalPrice/ticketNumber, ".2f"))
