class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, pay):
        Employee.__init__(self, name, number)
        self.__shift_number = shift_number
        self.__pay = pay

    def get_shift_number(self):
        return self.__shift_number

    def get_pay(self):
        return self.__pay

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay(self, pay):
        self.__pay = pay
