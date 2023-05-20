# Drawing letter 'A' in 1 dimension

# importing the module
import turtle

# creating a turtle object and assigning it to t
t = turtle.Turtle()
side = 100  # side lengths of letter 'A'

# initially the turtle points towards right
t.left(60)
# the turtle pointer will take a 60 degree turn
t.forward(side)
# draw length of one side of 'A'
t.right(180 - 60)
# turtle take a 120 degree turn from current direction of turtle
# so that there is a 60 degree angle between two sides of 'A'
t.forward(side)
# this will draw another side

# this part is to draw the middle line across two sides of 'A'
t.penup()
t.right(180)
t.forward(side / 2)
t.pendown()
t.left(60)
t.forward(side / 2)

# it calls Tkinter’s mainloop function
# so that window will stay open until the user exits the program
turtle.done()