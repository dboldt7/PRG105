import employee


def main():
    name = input("Enter the employees name ")
    number = input("Enter the employees ID number ")
    pay_rate = input("Enter the employees hourly wage ")
    shift_number = int(input('Enter the employees shift number '))
    data = employee.ProductionWorker(name, number, pay_rate, shift_number)
    print('Name: ' + data.get_name())
    print('Number: ' + data.get_number())
    print('Wage:', data.get_pay())
    if shift_number == 1:
        print('Day Shift')
    else:
        print('Night Shift')


main()
