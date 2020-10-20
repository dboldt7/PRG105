name_data = ["Daniel Boldt", 'John Doe', "Jane Doe"]
address_data = ["7100 Nighthawk Way", "123 Main Street", "321 West Drive"]
age_data = [18, 29, 65]
phone_data = ["847-778-5676", "847-909-1111", "847-120-5010"]


class PersonData:
    def __init__(self, name, ad, age, phone):
        self.__name = name
        self.__ad = ad
        self.__age = age
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_ad(self):
        return self.__ad

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_ad(self, ad):
        self.__ad = ad

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone


def mini_func(instance):  # Takes in an instance parameter so all the print statements are not repeated 3 times
    print(instance.get_name())
    print(instance.get_ad())
    print(instance.get_age())
    print(instance.get_phone())
    print('- - - - - - - - - - - - - -')


instance_1 = PersonData(name_data[0], address_data[0], age_data[0], phone_data[0])
mini_func(instance_1)

instance_2 = PersonData(name_data[1], address_data[1], age_data[1], phone_data[1])
mini_func(instance_2)

instance_3 = PersonData(name_data[2], address_data[2], age_data[2], phone_data[2])
mini_func(instance_3)
