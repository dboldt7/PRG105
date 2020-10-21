file = open('rainfall-totals.txt', 'r')

months_and_data = []
data_only = []
total = 0
divisor = 0

line = file.readline()
while line != '':
    refined_line = line.rstrip('\n')
    months_and_data.append(refined_line)
    line = file.readline()

for data in months_and_data:
    data_only.append(data[-3:])

for number in data_only:
    try:
        number = float(number)
        total = total + number
        divisor = divisor + 1
    except ValueError:
        print("There was an error processing this value: " + number)

print(format(total, '.2f'))
print(format(total / divisor, '.2f'))

file.close()
