accounts_list = []
over_list = []

try:
    file1 = open('accounts.txt', 'r')
except IOError:
    print("There was an error in opening this file")
    while not accounts_list:
        file1 = input("Restart the program and try again")

line = file1.readline()
while line != '':
    accounts_list.append(line.rstrip('\n'))
    line = file1.readline()

file1.close()

try:
    file2 = open('over90.txt', 'r')
except IOError:
    print("There was an error in opening a file")
    while not over_list:
        var = input("Restart the program and try again")

line = file2.readline()
while line != '':
    over_list.append(line.rstrip('\n'))
    line = file2.readline()

file2.close()

print("The following accounts are at least 90 days overdue:\n")

for account in accounts_list:
    for code in over_list:
        if code in account:
            print(account)
