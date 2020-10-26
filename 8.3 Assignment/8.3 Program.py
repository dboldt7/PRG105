accounts_list = []
over_list = []


def main_func():
    try:
        file1 = open('accounts.txt', 'r')

        line = file1.readline()
        while line != '':
            accounts_list.append(line.rstrip('\n'))
            line = file1.readline()

        file1.close()

        file2 = open('over90.txt', 'r')
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
    except IOError:
        print("There was a problem opening a file, restart and try again.")


main_func()
