input_data = input("Enter a string ")
words_list = input_data.split()
x = 0
final_acronym = ''
for word in words_list:
    words_list[x] = words_list[x].upper()
    words_list[x] = words_list[x][0]
    final_acronym = final_acronym + words_list[x]
    x = x + 1

print(final_acronym)
