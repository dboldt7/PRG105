array = ["Australia", "Brazil", "Canada", "Denmark", "Estonia", "Finland", "Georgia", "Hungary", "Iceland", "Jamaica",
         "Kazakhstan", "Latvia", "Morocco", "Nepal", "Oman", "Portugal", "Qatar", "Russia", "Suriname", "Turkey",
         "Uruguay", "Venezuela", " ", ".", "Yemen", "Zambia", "._.", "o_o", ">_>", "O_O"]

other_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', ' ', '!', '.', ',']


file = open('secret_codes.txt', 'w')

user_response = input("Say a phrase to be written in code ")

for letter in user_response:
    letter = letter.upper()
    index = other_list.index(letter)
    file.write(array[index] + '\n')

file.close()
