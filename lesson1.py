from turtle import *



#we want to paint a house
speed(30)
width(7)
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
end_fill()

#painting a door
color("orange")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()


width(7)
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
color("red")
forward(80)
color("blue")
begin_fill()
left(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
end_fill()

penup()
goto(200, 60)
pendown()
begin_fill()
forward(50)
right(90)
forward(60)
right(90)
forward(50)
penup()
end_fill()

exitonclick()
