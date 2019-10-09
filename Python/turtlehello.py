import turtle
frame=turtle.Screen().bgcolor("lavender")
draw=turtle.Turtle()
draw.color("black")
draw.speed(10)

#printing letter H
draw.left(90)
draw.forward(70)
print(draw.position())
draw.penup()
draw.goto(0,35)
draw.pendown()
draw.right(90)
draw.forward(30)
print(draw.position())
draw.penup()
draw.goto(30,70)
draw.pendown()
draw.right(90)
draw.forward(70)

#printing letter E

draw.penup()
draw.goto(40,0)
draw.pendown()
print(draw.position())
draw.right(180)
draw.forward(70)
draw.right(90)
draw.forward(35)
draw.penup()
draw.goto(40,35)
draw.pendown()
draw.forward(35)
draw.penup()
draw.goto(40,0)
draw.pendown()
draw.forward(35)
print(draw.position())

#printing letter L
draw.penup()
draw.goto(90,70)
draw.pendown()
draw.right(90)
draw.forward(70)
draw.left(90)
draw.forward(35)

#printing letter L
draw.penup()
draw.goto(135,70)
draw.pendown()
draw.right(90)
draw.forward(70)
draw.left(90)
draw.forward(35)

#printing letter O
draw.penup()
draw.goto(210,70)
draw.pendown()
for i in range(25):
    draw.right(15)
    draw.forward(10)
