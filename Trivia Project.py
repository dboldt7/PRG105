class Question:
    def __init__(self, question, ans1, ans2, ans3, ans4, answer):
        self.__question = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_ans1(self):
        return self.__ans1

    def get_ans2(self):
        return self.__ans2

    def get_ans3(self):
        return self.__ans3

    def get_ans4(self):
        return self.__ans4

    def get_answer(self):
        return self.__answer

    def set_question(self, question):
        self.__question = question

    def set_ans1(self, ans1):
        self.__ans1 = ans1

    def set_ans2(self, ans2):
        self.__ans2 = ans2

    def set_ans3(self, ans3):
        self.__ans3 = ans3

    def set_ans4(self, ans4):
        self.__ans4 = ans4

    def set_answer(self, answer):
        self.__answer = answer


q1 = Question('Which one of these countries lands border Brazil?', 'A. Chile', 'B. Ecuador', 'C. France', 'D. Nicaragua', 'C')
q2 = Question('Which one of these countries is located on the island of Hispaniola?', 'A Panama', 'B. Malaysia', 'C. Grenada',
              'D. Haiti', 'D')
q3 = Question("What country's flag has more than four points?", 'A. Nepal', 'B. Rwanda', 'C. Bolivia', 'D. Monaco', 'A')
q4 = Question("What is the most recent country to join the United Nations?", 'A. Nauru', 'B. East Timor', 'C. Bhutan', 'D. Suriname',
              'B')
q5 = Question("What country was supposed to host the 2020 Olympics?", 'A. Japan', 'B. Canada', 'C. Greece', 'D. Argentina', 'A')
q6 = Question("Which of these is not a country?", 'A. Togo', 'B. Greenland', 'C. Samoa', 'D. Dominica', 'B')
q7 = Question("Which one of these countries is located on the Iberian Peninsula?", 'A. Costa Rica', 'B. Mexico', 'C. Spain',
              'D. Denmark', 'C')
q8 = Question('By land mass, which country is the largest?', 'A. Canada', 'B. China', 'C. Russia', 'D. Australia', 'C')
q9 = Question('Which one of these nations exist partly in the Saharan Desert?', 'A. Angola', 'B. Madagascar', 'C. Liberia',
              'D. Chad', 'D')
q10 = Question('Which one of these countries does NOT border the Atlantic Ocean?', 'A. Morocco', 'B. Barbados', 'C. Paraguay',
               'D. Ireland', 'C')

p1_set = [q1, q2, q3, q4, q5]
p2_set = [q6, q7, q8, q9, q10]


def printing_func(query):
    print(query.get_question())
    print(query.get_ans1())
    print(query.get_ans2())
    print(query.get_ans3())
    print(query.get_ans4())


def main_func():
    p1_points = 0
    p2_points = 0

    for query in p1_set:
        printing_func(query)
        user_response = input("Enter the correct letter ").upper()
        if user_response == query.get_answer():
            p1_points = p1_points + 1

    for query in p2_set:
        printing_func(query)
        user_response = input("Enter the correct letter ").upper()
        if user_response == query.get_answer():
            p2_points = p2_points + 1

    if p1_points > p2_points:
        print("Player one has won with a score of", p1_points, "to", p2_points)
    elif p1_points < p2_points:
        print("Player two has won with a score of", p2_points, "to", p1_points)
    else:
        print("The players have tied, with both achieving a score of", p1_points)


main_func()
