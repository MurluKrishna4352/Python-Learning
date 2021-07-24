import turtle

#slowmo = turtle.Turtle()

slowmo = turtle.Pen()
#colour_list = ["red" , "yellow" , "cyan" , "orange", "green" , "black" , "pink" , "purple"]
slowmo.shape("turtle")
slowmo.speed(0)
slowmo.width(3)

# roseate pattern 
for i in range(100):
  #  slowmo.color(colour_list[i % 7])
    slowmo.circle(i+1)
    slowmo.left(15)

#for i in range(100000000):
   # slowmo.color(colour_list[i % 7])
    #slowmo.forward(i)
    #slowmo.left(90)



