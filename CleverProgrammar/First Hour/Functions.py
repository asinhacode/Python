import turtle
import tkinter

me_turtle = turtle.Turtle()  # declare object


def octagon():
    # made an octagon
    i = 0
    while i < 8:
        me_turtle.forward(100)
        me_turtle.right(45)  # change direction
        i += 1


# how to define functions
def square():
    j = 0
    while j < 4:
        me_turtle.forward(50)
        me_turtle.right(90)
        j += 1


# run the function

# octagon()
# me_turtle.forward(10)
# octagon()

square()
me_turtle.left(90)
square()

tkinter.mainloop()
