
class OfficeFurniture:
    def __init__(self,desk, material, length, width, height, price):
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price
        self.__desk = desk

    def get_material(self):
        return self.__material

    def __str__(self):
        return str("This piece of furniture is made out of " + self.__material)
