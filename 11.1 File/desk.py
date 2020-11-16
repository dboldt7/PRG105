import office_furniture


class Desk(office_furniture.OfficeFurniture):
    def __init__(self, desk, material, length, width, height, price, location_of_drawers, number_drawers):
        office_furniture.OfficeFurniture.__init__(self, desk, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def __str__(self):
        return str('This piece of furniture is made out of ' + office_furniture.OfficeFurniture.get_material(self)
                   + ' and holds ' + str(self.__number_drawers) + ' drawers on the ' + self.__location_of_drawers +
                   ' side')
