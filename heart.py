import turtle

# Create a screen
screen = turtle.Screen()

# Create a turtle
heart_turtle = turtle.Turtle()

# Function to draw a heart


def draw_heart(turtle_obj, size):
    turtle_obj.begin_fill()
    turtle_obj.fillcolor('red')
    turtle_obj.left(140)
    turtle_obj.forward(size)
    turtle_obj.circle(-50, 200)
    turtle_obj.left(120)
    turtle_obj.circle(-50, 200)
    turtle_obj.forward(size)
    turtle_obj.end_fill()


# Set initial position and orientation
heart_turtle.penup()
heart_turtle.goto(-50, 0)
heart_turtle.pendown()

# Draw a heart with size 100
draw_heart(heart_turtle, 100)

# Hide the turtle
heart_turtle.hideturtle()

# Keep the window open
screen.mainloop()
