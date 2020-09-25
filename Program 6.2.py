def avg_func(total, entries):
    average = total / entries
    print("The average value was", format(average, ',.2f'))


def main_func():
    file = open('sales_totals-1.txt', 'r')
    line = file.readline()
    number_of_lines = 0
    total = 0

    while line != '':
        refined_line = float(line.rstrip('\n'))
        print(line)
        number_of_lines = number_of_lines + 1
        total = total + refined_line
        line = file.readline()
    print("The total was", format(total, ',.2f'))
    print("The number of entries was", number_of_lines)
    avg_func(total, number_of_lines)
    file.close()


main_func()
