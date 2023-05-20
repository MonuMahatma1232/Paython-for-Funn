import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the turtle position and pen color
my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()
my_turtle.pencolor('red')

# Draw the message
my_turtle.write("I Love U Gowri", font=("Arial", 18, "bold"))

# Move the turtle to draw the heart
my_turtle.penup()
my_turtle.goto(0, -50)
my_turtle.pendown()
my_turtle.begin_fill()

# Draw the heart
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.circle(50, 180)
my_turtle.right(90)
my_turtle.circle(50, 180)
my_turtle.forward(100)

# End the fill and hide the turtle cursor
my_turtle.end_fill()
my_turtle.hideturtle()

# Draw the "With ❤️" message
my_turtle.penup()
my_turtle.goto(10, -100)
my_turtle.pendown()
my_turtle.write("With ❤️", font=("Arial", 18, "bold"))

# Exit on click
turtle.exitonclick()
