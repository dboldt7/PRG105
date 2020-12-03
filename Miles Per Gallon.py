import tkinter


class TheGui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bot_frame = tkinter.Frame()

        self.gallon_text = tkinter.Label(self.top_frame, text="Enter number of gallons")
        self.gallon_entry = tkinter.Entry(self.top_frame, width=10)

        self.gallon_text.pack(side='left')
        self.gallon_entry.pack(side='left')

        self.miles_text = tkinter.Label(self.mid_frame, text="Enter number of miles")
        self.miles_entry = tkinter.Entry(self.mid_frame, width=10)

        self.miles_text.pack(side='left')
        self.miles_entry.pack(side='left')

        self.final_value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.bot_frame, textvariable=self.final_value)

        self.convert_button = tkinter.Button(self.bot_frame, text='Convert', command=self.convert_function)
        self.quit_button = tkinter.Button(self.bot_frame, text='Quit', command=self.main_window.destroy)

        self.results_label.pack(side='top')
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()
        tkinter.mainloop()

    def convert_function(self):
        gallons_amt = float(self.gallon_entry.get())
        miles_amt = float(self.miles_entry.get())
        value = format(miles_amt/gallons_amt, '.2f')
        self.final_value.set(value + ' mile(s) per gallon')


test = TheGui()
