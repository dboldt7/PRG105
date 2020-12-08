import tkinter
import random
import tkinter.font as tk_font
choices = ['Rock', 'Paper', 'Scissors']
outcomes = ('You win', 'You lose', 'Tie')


class MainGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # Sets all the frames up
        self.title_frame = tkinter.Frame()
        self.CPU_response_frame = tkinter.Frame()
        self.label_scores_frame = tkinter.Frame()
        self.scores_frame = tkinter.Frame()
        self.outcome_frame = tkinter.Frame()
        self.buttons_frame = tkinter.Frame()
        # Setting Title up
        font_style = tk_font.Font(family="Lucida Grande", size=15)
        self.title_text = tkinter.Label(self.title_frame, text='ROCK PAPER SCISSORS', font=font_style)
        self.title_text.pack()
        self.title_frame.pack()

        self.CPU_label = tkinter.Label(self.title_frame, text="Computer chose")

        self.CPU_response = tkinter.StringVar()
        self.CPU_answer = tkinter.Label(self.CPU_response_frame, textvariable=self.CPU_response)

        self.player_score = tkinter.StringVar()
        self.CPU_score = tkinter.StringVar()
        self.player_score_on_screen = tkinter.Label(self.scores_frame, textvariable=self.player_score)
        self.CPU_score_on_screen = tkinter.Label(self.scores_frame, textvariable=self.CPU_score)

        self.Testing_Label = tkinter.Label(self.label_scores_frame, text='CPU Wins', padx=25)
        self.Testing_Label2 = tkinter.Label(self.label_scores_frame, text='Player Wins', padx=25)
        self.Testing_Label.pack(side='left')
        self.Testing_Label2.pack(side='right')

        self.result = tkinter.StringVar()
        self.final_result = tkinter.Label(self.outcome_frame, textvariable=self.result)
        # Sets up buttons
        self.rock_button = tkinter.Button(self.buttons_frame, text='Rock', command=lambda: self.rock_func('Rock'))
        self.paper_button = tkinter.Button(self.buttons_frame, text='Paper', command=lambda: self.rock_func('Paper'))
        self.scissors_button = tkinter.Button(self.buttons_frame, text='Scissors', command=lambda: self.rock_func('Scissors'))
        self.start_button = tkinter.Button(self.outcome_frame, text='START', command=self.start_func)
        # Packs misc. items needs to be cleaned up
        self.start_button.pack()
        self.CPU_answer.pack()
        self.final_result.pack()
        self.player_score_on_screen.pack(side='right', padx=45)
        self.CPU_score_on_screen.pack(side='left', padx=45)

        self.title_frame.pack()
        self.CPU_response_frame.pack()
        self.label_scores_frame.pack()
        self.scores_frame.pack()
        self.outcome_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def rock_func(self, user_choice):
        cpu_choice = choices[random.randint(0, 2)]
        self.CPU_response.set(cpu_choice)

        if user_choice == 'Rock':
            if cpu_choice == 'Scissors':
                print("User Wins!")
                self.user_win_function()
            elif cpu_choice != 'Rock':
                print('CPU Wins!')
                self.cpu_win_function()
        if user_choice == 'Paper':
            if cpu_choice == 'Rock':
                print("User Wins!")
                self.user_win_function()
            elif cpu_choice != 'Paper':
                print('CPU Wins!')
                self.cpu_win_function()
        if user_choice == 'Scissors':
            if cpu_choice == 'Paper':
                print("User Wins!")
                self.user_win_function()
            elif cpu_choice != 'Scissors':
                print('CPU Wins!')
                self.cpu_win_function()
        if user_choice == cpu_choice:
            print("It's a tie!")
            self.result.set("Tied!")
        # Is there a better way to go about determining the winner without the if/else statements?

    def start_func(self):
        self.start_button.destroy()
        self.rock_button.pack(side='left')
        self.paper_button.pack(side='left')
        self.scissors_button.pack(side='left')
        self.CPU_label.pack(side='bottom')
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
            file = open('Record.txt', 'w')
            file.close()
            self.CPU_score.set(0)
            self.player_score.set(0)

    def user_win_function(self):
        local_file = open('Record.txt', 'a')
        local_file.write('1\n')
        local_file.close()
        current_user_score = int(self.player_score.get()) + 1
        self.player_score.set(str(current_user_score))
        self.result.set("You win!")

    def cpu_win_function(self):
        local_file = open('Record.txt', 'a')
        local_file.write('0\n')
        local_file.close()
        current_cpu_score = int(self.CPU_score.get()) + 1
        self.CPU_score.set(str(current_cpu_score))
        self.result.set("You lost!")

# Is there a way to integrate the CPU_win_function with the user_win_function?


test = MainGui()
