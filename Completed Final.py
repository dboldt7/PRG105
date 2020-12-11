import tkinter
import random
# Credit for importing tkinter.font and usage of tkinter.font: https://pythonexamples.org/python-tkinter-button-change-font/
import tkinter.font as tk_font


class MainGui:
    def __init__(self):
        # Sets up main window
        self.main_window = tkinter.Tk()

        # Variables that are used later in the class
        self.previous_cpu_choice = None
        self.tie_instance = ParentClass('Tie')
        self.user_win_instance = UserWin()
        self.CPU_win_instance = CpuWin()

        # Sets all the frames up
        self.title_frame = tkinter.Frame()
        self.CPU_response_frame = tkinter.Frame()
        self.label_scores_frame = tkinter.Frame()
        self.scores_frame = tkinter.Frame()
        self.outcome_frame = tkinter.Frame()
        self.buttons_frame = tkinter.Frame()

        # Two different data types being used
        self.frames_tuple = (self.title_frame, self.CPU_response_frame, self.label_scores_frame, self.scores_frame, self.outcome_frame,
                             self.buttons_frame)
        self.choices_list = ['Rock', 'Paper', 'Scissors']

        # Font Styles
        title_font_style = tk_font.Font(family="Helvetica", size=15, underline=True)
        start_font_style = tk_font.Font(family="Helvetica", size=20)
        outcome_font_style = tk_font.Font(family='Verdana', weight='bold')

        # Setting up Title Frame
        self.title_text = tkinter.Label(self.title_frame, text='ROCK PAPER SCISSORS', font=title_font_style)
        self.CPU_label = tkinter.Label(self.title_frame, text="Computer chose:")
        self.title_frame.pack()
        self.title_text.pack()

        # Setting up CPU Response Frame
        self.CPU_response = tkinter.StringVar()
        self.CPU_answer = tkinter.Label(self.CPU_response_frame, textvariable=self.CPU_response)
        self.CPU_answer.pack()

        # Setting up Label Scores Frame
        self.player_wins_text_label = tkinter.Label(self.label_scores_frame, text='CPU Wins', padx=25)
        self.cpu_wins_text_label = tkinter.Label(self.label_scores_frame, text='Player Wins', padx=25)

        # Setting up Scores Frame
        self.player_score = tkinter.StringVar()
        self.CPU_score = tkinter.StringVar()

        self.player_score_on_screen = tkinter.Label(self.scores_frame, textvariable=self.player_score)
        self.CPU_score_on_screen = tkinter.Label(self.scores_frame, textvariable=self.CPU_score)

        self.player_score_on_screen.pack(side='right', padx=50)
        self.CPU_score_on_screen.pack(side='left', padx=50)

        # Setting up Outcome Frame
        self.result = tkinter.StringVar()
        self.final_result = tkinter.Label(self.outcome_frame, textvariable=self.result, font=outcome_font_style)
        self.final_result.pack()

        # Sets up Player Buttons
        # Credit for lambda usage: https://youtu.be/Y6cir7P3YUk?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk
        # Credit for changing color of button: https://pythonexamples.org/python-tkinter-button-background-color/
        self.rock_button = tkinter.Button(self.buttons_frame, text='Rock', command=lambda: self.secondary_func('Rock'), bg='light gray')
        self.paper_button = tkinter.Button(self.buttons_frame, text='Paper', command=lambda: self.secondary_func('Paper'), bg='light gray')
        self.scissors_button = tkinter.Button(self.buttons_frame, text='Scissors', command=lambda: self.secondary_func('Scissors'), bg='light gray')

        # Sets up Start Button
        self.start_button = tkinter.Button(self.CPU_response_frame, text='START', command=self.start_func, bg='light yellow', font=start_font_style)
        self.start_button.pack()

        # Packs all the frames in one loop
        for frame in self.frames_tuple:
            frame.pack()

        tkinter.mainloop()

    def secondary_func(self, user_choice):
        # Determines the CPU's response and displays it onscreen
        cpu_choice = self.choices_list[random.randint(0, 2)]
        if self.previous_cpu_choice == cpu_choice:
            cpu_choice = self.choices_list[random.randint(0, 2)]
        self.previous_cpu_choice = cpu_choice
        self.CPU_response.set(cpu_choice)

        if user_choice == 'Rock':
            if cpu_choice == 'Scissors':
                self.user_win_function()
            elif cpu_choice != 'Rock':
                self.cpu_win_function()
        if user_choice == 'Paper':
            if cpu_choice == 'Rock':
                self.user_win_function()
            elif cpu_choice != 'Paper':
                self.cpu_win_function()
        if user_choice == 'Scissors':
            if cpu_choice == 'Paper':
                self.user_win_function()
            elif cpu_choice != 'Scissors':
                self.cpu_win_function()
        if user_choice == cpu_choice:
            self.final_result.configure(fg='goldenrod')
            self.result.set(self.tie_instance.result())

    def start_func(self):
        self.start_button.destroy()

        self.rock_button.pack(side='left')
        self.paper_button.pack(side='left')
        self.scissors_button.pack(side='left')

        self.CPU_label.pack(side='bottom')
        self.player_wins_text_label.pack(side='left')
        self.cpu_wins_text_label.pack(side='right')
        # Loop attempts to open a file, read its contents, and display the scores on screen
        try:
            player_win_count = 0
            cpu_win_count = 0
            file = open('Record.txt', 'r')
            line = file.readline()
            while line != '':
                clean_line = line.rstrip('\n')
                if clean_line == '1':
                    player_win_count = player_win_count + 1
                elif clean_line == '0':
                    cpu_win_count = cpu_win_count + 1
                line = file.readline()
            self.CPU_score.set(str(cpu_win_count))
            self.player_score.set(str(player_win_count))
        except FileNotFoundError:
            # Sets both scores to start at 0
            self.CPU_score.set(0)
            self.player_score.set(0)

            # Creates the file because one was not found
            file = open('Record.txt', 'w')
            file.close()

    def user_win_function(self):
        # Just adds the player win to the GUI and shows outcome does NOT involve file
        current_user_score = int(self.player_score.get()) + 1
        self.player_score.set(str(current_user_score))
        self.final_result.configure(fg='green3')
        self.result.set(self.user_win_instance.result())

        # Writes to the file a 1 representing a player win
        local_file = open('Record.txt', 'a')
        local_file.write('1\n')
        local_file.close()

    def cpu_win_function(self):
        # Just adds the CPU win to the GUI and shows outcome does NOT involve file
        current_cpu_score = int(self.CPU_score.get()) + 1
        self.CPU_score.set(str(current_cpu_score))
        self.final_result.configure(fg='red4')
        self.result.set(self.CPU_win_instance.result())

        # Writes to the file a 0 representing a computer win
        local_file = open('Record.txt', 'a')
        local_file.write('0\n')
        local_file.close()


class ParentClass:
    def __init__(self, result):
        self.__result = result

    def result(self):
        return 'Tied'


class UserWin(ParentClass):
    def __init__(self):
        ParentClass.__init__(self, 'You win!')

    def result(self):
        return 'You win!'


class CpuWin(ParentClass):
    def __init__(self):
        ParentClass.__init__(self, 'You lost!')

    def result(self):
        return 'You lost!'


test = MainGui()
