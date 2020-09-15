def main_func():
    print("Please select a movie from below")
    print("A. The Godfather")
    print("B. Wall-E")
    print("C. The Martian")
    print("D. Pulp Fiction")
    print("E. Jaws")
    letter = input("Enter the letter of your choice. ")
    if letter == "A":
        a()
    elif letter == "B":
        b()
    elif letter == "C":
        c()
    elif letter == "D":
        d()
    else:
        e()


def a():
    print("This movie is rated R and is playing on screen 12.")


def b():
    print("This movie is rated G and is playing on screen 19.")


def c():
    print("This movie is rated PG-13 and is playing on screen 4.")


def d():
    print("This movie is rated R and is playing on screen 1.")


def e():
    print("This movie is rated PG and is playing on screen 7.")


main_func()



