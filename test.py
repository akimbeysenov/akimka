import turtle
def draw_rainbow_circle():
 colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
 turtle.speed(0)
 for i in range(180):
    for color in colors:
        turtle.color(color)
        turtle.forward(2)
        turtle.right(1)
    turtle.right(2)
 turtle.done()
draw_rainbow_circle()