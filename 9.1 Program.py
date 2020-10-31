main_dictionary = {'Sunday': '', 'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday': '',
                   'Saturday': ''}

total_steps = 0
for key in main_dictionary:
    local_steps = int(input("Please enter the number of steps taken on " + key + ': '))
    main_dictionary[key] = local_steps
    total_steps = total_steps + local_steps


average = total_steps / 7
print("The average amount of steps was: ", format(average, '.1f'))
print("The total amount of steps taken this week was ", total_steps)
