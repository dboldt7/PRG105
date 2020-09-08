
totalSales = 0

for day in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
    amt = float(input("How much did you sell on " + day + "? "))
    totalSales = totalSales + amt

print("The total sales for this week was $", format(totalSales, ".2f"))
print("The average amount of sales per day was $", format(totalSales/7, ".2f"))
