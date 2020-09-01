""""
Banana Bread Recipe:
2 cups of flour
1 teaspoon of baking soda
0.25 teaspoons of salt
0.5 cups of butter
0.75 cups of brown sugar
2 eggs
2.33 bananas

Recipe produces 12 servings of bread
Write a program that asks the user how many servings they want
Program displays the ingredients needed to make the desired amount
"""
Servings = 12
Flour = 2
bakingSoda = 1
salt = 0.25
butter = 0.5
sugar = 0.75
egg = 2
banana = 2.33

desiredServings = int(input("How many servings do you want? "))
percentChange = (desiredServings - Servings) / Servings

if percentChange == 0:
    percentChange = 1
elif percentChange > 0:
    percentChange = 1 + percentChange
else:
    percentChange = percentChange * -1
print("")
print("Ingredients Needed:\n")
print((Flour * percentChange), " cups of flour")
print(format(bakingSoda * percentChange, ".1f"), "teaspoons of baking soda")
print(format(salt * percentChange, ".1f"), " teaspoons of salt")
print(format(butter * percentChange, ".1f"), " cups of butter")
print(format(sugar * percentChange, ".1f"), " cups of sugar")
print(format(egg * percentChange, ".1f"), " eggs")
print(format(banana * percentChange, ".1f"), " bananas")
