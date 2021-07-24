import turtle
a = turtle.Turtle()
a.shape("turtle")
a.speed(0)
a.width(1.9)
wn = turtle.Screen()
wn.bgcolor("indigo")
a.color("turquoise")

def unkown_shape(length,angle):
    for j in range(4):
        a.backward(length)
        a.right(45)
        a.forward(length)
        a.left(angle)

for j in range(100):
    unkown_shape(100,299)
    a.forward(10.5457987654987985)
    a.right(280)