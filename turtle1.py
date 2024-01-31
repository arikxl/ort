import turtle
# Create a screen
screen = turtle.Screen()
screen.bgcolor('hotPink')

# Create a turtle
player = turtle.Turtle()
player.shape('turtle')
# arrow, square, circle, triangle, blank 
player.pensize(7)
player.pencolor('lime')
player.color('deepskyblue')

player.speed(1)
# 1-10

player.begin_fill()
player.fillcolor('red')
# Move the turtle forward by 100 units
player.forward(100)

# Rotate the turtle clockwise by 90 degrees
player.left(90)

# Move the turtle forward by 100 units again
player.forward(100)

player.end_fill()

# Close the turtle graphics window when clicked
screen.exitonclick()

turtle.done()