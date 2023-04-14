import turtle
tao = turtle.Pen()


def rectangle(width):
    for i in range(4):
        tao.fd(width)
        tao.left(90)

def go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

for i in range(10):
    rectangle(100)
    tao.left(36)

for i in range(10):
    tao.circle(100)
    tao.left(36)
    
go(0,-100)
tao.right(90)
tao.fd(300)
