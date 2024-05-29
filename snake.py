import turtle
import random

# Set up the screen
win = turtle.Screen()
win.title("Turtle Game")
win.bgcolor("lightblue")
win.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the food item
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Create the score display
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center",
                    font=("Courier", 24, "normal"))

# Define player movement functions


def go_up():
    if player.heading() != 270:
        player.setheading(90)


def go_down():
    if player.heading() != 90:
        player.setheading(270)


def go_left():
    if player.heading() != 0:
        player.setheading(180)


def go_right():
    if player.heading() != 180:
        player.setheading(0)


# Keyboard bindings
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Main game loop
while True:
    win.update()
    player.forward(1)

    # Check for collision with food
    if player.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        score += 1
        score_display.clear()
        score_display.write(
            f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with border
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        player.goto(0, 0)
        player.direction = "stop"
        score = 0
        score_display.clear()
        score_display.write(
            f"Score: {score}", align="center", font=("Courier", 24, "normal"))
