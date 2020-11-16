import office_furniture
import desk


def main():
    test = office_furniture.OfficeFurniture(1, 'Wood', '72 Inches', '48 Inches', '16 Inches', '$2000')
    test2 = desk.Desk(1, 'Wood', '72 Inches', '48 Inches', '16 Inches', '$2000', 'Right', 24)
    print(test)
    print(test2)


main()
