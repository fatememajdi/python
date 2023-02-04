import turtle

my_turtle_screen = turtle.getscreen()

t = turtle.Turtle()
t.shape("turtle")


def DrawShape(n, l):
    angle = (180*(n-2))/n
    t.right(-(180 - (angle/2)))
    t.forward(l)
    for _ in range(n-1):
        t.left(180-angle)
        t.forward(l)
    t.penup()
    t.right(angle/2)
    t.forward(20)
    t.pendown()


DrawShape(3, 50)
DrawShape(4, 70)
DrawShape(5, 80)
DrawShape(6, 90)
DrawShape(7, 100)
DrawShape(8, 105)
DrawShape(9, 110)
DrawShape(10, 115)
