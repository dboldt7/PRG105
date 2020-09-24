def main_func():
    the_file = open('contact_info.txt', 'w')
    number_of_entries = int(input("How many entries do you want to make? "))
    for count in range(1, number_of_entries + 1):
        name = input("What is their name? ")
        phone = input("What's their phone number? ")
        email = input("What's their email address? ")
        the_file.write(name + ', ')
        the_file.write(phone + ', ')
        the_file.write(email + '\n')
    the_file.close()


main_func()
