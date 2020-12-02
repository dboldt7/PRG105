
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.Data_Frame = tkinter.Frame(self.main_window)
        self.Buttons_Frame = tkinter.Frame(self.main_window)

        self.name = tkinter.StringVar()
        self.add1 = tkinter.StringVar()
        self.add2 = tkinter.StringVar()

        self.label1 = tkinter.Label(self.Data_Frame, textvariable=self.name)
        self.label2 = tkinter.Label(self.Data_Frame, textvariable=self.add1)
        self.label3 = tkinter.Label(self.Data_Frame, textvariable=self.add2)

        self.label1.pack()
        self.label2.pack()
        self.label3.pack()

        self.show_info_button = tkinter.Button(self.Buttons_Frame, text="show info", command=self.show)
        self.delete_button = tkinter.Button(self.Buttons_Frame, text="quit", command=self.main_window.destroy)

        self.show_info_button.pack(side='left')
        self.delete_button.pack(side='left')

        self.Data_Frame.pack()
        self.Buttons_Frame.pack()

        tkinter.mainloop()

    def show(self):
        self.name.set('Dan Boldt')
        self.add1.set('1600 Pennsylvania Avenue NW')
        self.add2.set('Washington, D.C. 20500')


display = MyGUI()
