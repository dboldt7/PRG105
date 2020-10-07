x = 3
array = ["Australia", "Brazil", "Canada", "Denmark", "Estonia", "Finland", "Georgia", "Hungary", "Iceland", "Jamaica",
         "Kazakhstan", "Latvia", "Morocco", "Nepal", "Oman", "Portugal", "Qatar", "Russia", "Suriname", "Turkey",
         "Uruguay", "Venezuela", " ", ".", "Yemen", "Zambia", "._.", "o_o", ">_>", "O_O"]

other_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', ' ', '!', '.', ',']

file = input("What's the name of the file you want to decode? ")

while x == 3:
    try:
        open(file, 'r')
        break
    except IOError:
        file = input("Try again, enter a file ")

file = open(file, 'r')
line = file.readline()
message = ''

while line != '':
    refined_line = line.rstrip('\n')
    index = array.index(refined_line)
    equivalent_letter = other_list[index]
    message = message + equivalent_letter
    line = file.readline()

print(message)

file.close()
