import turtle


t = turtle.Pen()
direct = 'up'


def check(sum):
    if (direct == 'right'):
        t.left(sum)
    elif (direct == 'left'):
        t.left(sum+180)
    elif (direct == 'down'):
        t.left(sum+90)
    else:
        t.left(sum-90)

def up():
    check(90)
    t.forward(30)
    newdir='up'
    return(newdir)

def left():
    check(180)
    t.forward(30)
    newdir='left'
    return(newdir)

def down():
    check(270)
    t.forward(30)
    newdir='down'
    return(newdir)


def right():
    check(0)
    t.forward(30)
    newdir='left'
    return(newdir)

# def right():
#     if (direct=='left'):
#         t.left(180)
#         t.forward(30)
#     elif (direct=='up'):
#         t.left(-90)
#         t.forward(30)
#     elif(direct=='down'):
#         t.left(90)
#         t.forward(30)
#     else:
#         t.forward(30)
#     newdir='right'
#     return(newdir)
#
#
# def left():
#     if (direct=='right'):
#         t.left(180)
#         t.forward(30)
#     elif (direct=='up'):
#         t.left(90)
#         t.forward(30)
#     elif(direct=='down'):
#         t.left(-90)
#         t.forward(30)
#     else:
#         t.forward(30)
#     newdir='left'
#     return(newdir)
#
#
# def up():
#     if (direct=='down'):
#         t.left(180)
#         t.forward(30)
#     elif (direct=='left'):
#         t.left(-90)
#         t.forward(30)
#     elif(direct=='right'):
#         t.left(90)
#         t.forward(30)
#     else:
#         t.forward(30)
#     newdir='up'
#     return(newdir)
#
#
# def down():
#     if (direct=='up'):
#         t.left(180)
#         t.forward(30)
#     elif (direct=='left'):
#         t.left(-90)
#         t.forward(30)
#     elif(direct=='right'):
#         t.left(90)
#         t.forward(30)
#     else:
#         t.left(-90)
#         t.forward(30)

t.shape('turtle')
direct=turtle.onkeypress(up, 'Up')
direct=turtle.onkeypress(right, 'Right')
direct=turtle.onkeypress(left, 'Left')
direct=turtle.onkeypress(down, 'Down')
direct=turtle.listen()



