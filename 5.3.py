pi_num = 3.14


def main_func():
    secondary()
    input1 = int(input("Select the corresponding number "))
    validated_input = check_function(input1)
    if validated_input == 5:
        return 5
    else:
        shape(validated_input)


def check_function(placeholder):
    local_number = placeholder
    if 1 <= local_number <= 5:
        return local_number
    else:
        while local_number > 5 or local_number < 1:
            local_number = int(input("Try again, enter a whole number between 1 and 5 "))
        return local_number


def shape(num):
    if num == 1:
        width = int(input("What is the rectangle's width? "))
        length = int(input("What is the rectangles height? "))
        print("Your shape's area is ", int(width * length))
    elif num == 2:
        width = int(input("What is the triangle's height? "))
        length = int(input("What is your triangle's width? "))
        print("Your shape's area is", format(0.5 * width * length, '.2f'))
    elif num == 3:
        width = int(input("What is the length of one side of the square? "))
        print("Your square's area is ", format(width ** 2, '.2f'))
    elif num == 4:
        width = int(input("What is the length of the radius of the circle? "))
        width = width ** 2
        print("Your circle's area is ", format(3.14 * width, '.2f'))
    else:
        print('')


def secondary():
    print("This program will find the area of a shape for you.")
    print("1.) Rectangle")
    print("2.) Triangle")
    print("3.) Square")
    print("4.) Circle")
    print("5.) Quit")


while pi_num == 3.14:
    if main_func() == 5:
        break
    else:
        main_func()
