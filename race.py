import turtle
import random

colors = ['red','blue','orange','cyan','brown','green','purple','black','gray','pink']

racers = int(input("How many turtles do you want to race? (2-10) "))
turtles = []

def create_screen():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.title('RACE')


random.shuffle(colors)
random_colors = colors[:racers]

# [1,2,3,4,5,99][:3]
# [1,2,3]

print(random_colors)

# racer = turtle.Turtle()
# racer.shape('turtle')
# racer.fd(100)
# racer.speed(2)
# racer.color('brown')

def create_turtles(list):

    posX = 500// (len(list) +1)

    for color in list:
        index = list.index(color)
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)

        racer.penup()
        racer.setpos(-250+( index +1) * posX, -250 +20)
        racer.pendown()

        turtles.append(racer)


create_turtles(random_colors)

def race():
    while True:
        for racer in turtles:
            speed = random.randint(1,20)
            racer.forward(speed)
            x,y = racer.pos()
            if y > 250 -10:
                winner= random_colors[turtles.index(racer)]
            # ['blue','red']
            # [turtle1, turtle2]
                # 0           1
                print(winner)
                return

race()
# print(winner)
turtle.done()