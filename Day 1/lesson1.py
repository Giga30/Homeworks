from turtle import *

width(5)
speed(30)
color('red')

#Drawing the house

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(30)
begin_fill()

forward(200)
right(120)

forward(200)
end_fill()
right(30)

forward(200)
right(90)

forward(80)
color('yellow')
right(90)

forward(70)
left(90)

forward(40)
left(90)

forward(70)
left(90)

forward(40)
right(180)
color('red')
penup()

forward(40)
pendown()
forward(80)

#Drawing windows

penup()
goto(20, -60)
pendown()

right(180)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)
right(90)



penup()
goto(180, -100)
pendown()

right(180)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)
right(90)


exitonclick()
