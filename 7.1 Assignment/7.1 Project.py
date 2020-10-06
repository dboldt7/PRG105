number_of_students = int(input("How many students are in your class? "))
running_list = []
for i in range(0, number_of_students):
    child = str(input("Enter the child's name "))
    grade = str(input("Enter the child's grade "))
    data = running_list.append([child, grade])

file = open('child.txt', 'w')

for i in range(0, number_of_students):
    file.write(running_list[i][0] + ": " + running_list[i][1] + '\n')

file.close()
