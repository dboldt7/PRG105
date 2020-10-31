def main_func():
    dictionary = {'Uno': 'One', 'Dos': 'Two', 'Tres': 'Three', 'Cuatro': 'Four', 'Cinco': 'Five', 'Seis': 'Six',
                  'Siete': 'Seven', 'Ocho': 'Eight', 'Nueve': 'Nine', 'Diez': 'Ten'}

    total_correct = 0

    for key in dictionary:
        user_response = input('What is the equivalent of: ' + key + '\n')
        if user_response == dictionary[key]:
            total_correct = total_correct + 1
            print("Correct")
        else:
            print("Incorrect")

    if total_correct <= 5:
        grade = 'F'
    elif total_correct <= 6:
        grade = 'D'
    elif total_correct <= 7:
        grade = 'C'
    elif total_correct <= 8:
        grade = 'B'
    else:
        grade = 'A'

    print("You scored", total_correct, "out of 10")
    print("Your grade is a(n) " + grade)


main_func()
