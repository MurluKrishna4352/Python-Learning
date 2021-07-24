import turtle
t = turtle.Pen()
t.speed(0)
wn=turtle.Screen()
wn.bgcolor("black")
t.shape("turtle")
t.color("red")
colourlist = ["red" "blue" "green" "yellow"]

for i in range(100):
    t.color(colorlist(i%4))
    t.forward(100)
    t.right(225)
