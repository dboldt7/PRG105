def avg_func(total, entries):
    average = total / entries
    print("The average value was", format(average, ',.2f'))


def main_func():
    try:
        open('sales_error.txt', 'r')
    except IOError:
        print("There was an error reading the file")
    file = open('sales_error.txt', 'r')
    line = file.readline()
    number_of_lines = 0
    total = 0

    while line != '':
        try:
            float(line.rstrip('\n'))

        except ValueError:
            print("ERROR\n")
            line = file.readline()
        refined_line = float(line.rstrip('\n'))
        print(line)
        number_of_lines = number_of_lines + 1
        total = total + refined_line
        line = file.readline()
    print("The total was", format(total, ',.2f'))
    print("The number of valid entries were", number_of_lines)
    avg_func(total, number_of_lines)
    file.close()


main_func()
