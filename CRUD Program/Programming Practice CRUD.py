import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open('customer_file.dat', 'br')
        customers = pickle.load(input_file)
    except(FileNotFoundError, IOError):
        print("File not found")
        customers = {}

    choice = 0

    while choice != QUIT:
        choice = menu()

        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)
        elif choice == CHANGE:
            change(customers)


def menu():
    print('Customer phone lookup')
    print('1. Look up a customer')
    print('2. Add a new customer')
    print('3. Change a phone number')
    print('4. Delete a customer')
    print('5. Quit the program')

    choice = int(input('Enter a number '))
    while choice < 1 or choice > 5:
        choice = int(input('Enter a valid number '))
    return choice


def look_up(customers):
    name = input('Enter a customer name: ')
    print(customers.get(name, 'Not Found'))


def add(customers):
    name = input("Enter the customers name: ")
    phone = input("Enter the customers phone number ")
    if name not in customers:
        customers[name] = phone
    else:
        print("That entry already exists")


def change(customers):
    name = input("Enter the customer's name: ")
    if name in customers:
        phone = input("Enter the customer's new phone number ")
        customers[name] = phone
    else:
        print("That customer was not found")


def delete(customers):
    name = input("Enter the customer's name: ")
    if name in customers:
        del customers[name]
    else:
        print("The customer was not located")


def save(customers):
    print("The file has been updated with your changes")
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()


main()
