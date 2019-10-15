import turtle as trtl

drawer = trtl.Turtle()
drawer.pendown()

drawer.color("gray")
# trtl.shape("triangle")
# trtl.shapesize("50")

drawer.penup()
drawer.goto(0, 200)
drawer.pendown()


drawer.penup()
drawer.goto(10, 0)
drawer.pendown()
drawer.fillcolor("dark blue")
drawer.begin_fill()
drawer.setheading(150)
drawer.forward(400)
drawer.left(200)
drawer.forward(358)
drawer.end_fill()


drawer.penup()
drawer.goto(10, 0)
drawer.pendown()
drawer.fillcolor("dark blue")
drawer.begin_fill()
drawer.setheading(-150)
drawer.forward(-400)
drawer.left(-200)
drawer.forward(-358)
drawer.end_fill()

drawer.penup()
drawer.goto(60, 60)
drawer.pendown()
drawer.fillcolor("dark blue")
drawer.begin_fill()
drawer.setheading(100)
drawer.forward(300)
drawer.left(155)
drawer.forward(280)
drawer.end_fill()

count = 1
while (count < 3)
drawer.pendown()
drawer.goto(0,0)
drawer.shape("circle")
drawer.circle(48)


# count = 0
# while count < 3:
#     drawer.forward(50)
#     drawer.right(120)
#     count = count + 1


wn = trtl.Screen()
wn.mainloop()