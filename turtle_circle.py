from pickle import TRUE
import turtle

t=turtle.Pen()

def circle():
    for i in range(360):
        t.forward(1)
        t.left(1)


turtle.onkeypress(circle, 'c')
turtle.listen()
circle()

