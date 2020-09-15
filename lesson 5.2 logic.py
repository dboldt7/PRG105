number = int(input("Enter a whole number between 20 and 100 "))


def divide_two(num):
    if num % 2 == 0:
        print(num, "is divisible by 2")
    else:
        print(num, "is not divisible by 2")


def divide_three(num):
    if num % 3 == 0:
        print(num, "is divisible by 3")
    else:
        print(num, "is not divisible by 3")


def divide_five(num):
    if num % 5 == 0:
        print(num, "is divisible by 5")
    else:
        print(num, "is not divisible by 5")


def main_func():
    final_num = check_function(number)
    divide_two(final_num)
    divide_three(final_num)
    divide_five(final_num)


def check_function(placeholder):
    local_number = placeholder
    if 20 < local_number < 100:
        return local_number
    else:
        while local_number > 100 or local_number < 20:
            local_number = int(input("Try again, enter a whole number between 20 and 100 "))
        return local_number


main_func()
