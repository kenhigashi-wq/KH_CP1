#KH turtle race second
import random, turtle


def setup():
    # import the stuff, turtle and random
    
    #Set turtle racer variables
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t5 = turtle.Turtle()
    t1.shape("turtle")
    t2.shape("turtle")
    t3.shape("turtle")
    t4.shape("turtle")
    t5.shape("turtle")
    #Also define the shape
    #Set their colors
    t1.color("red")
    t2.color("blue")
    t3.color("green")
    t4.color("yellow")
    t5.color("pink")
    #Set up the screen
    screen = turtle.Screen()
    screen.setup(600,400)
    # Set the indivisual guys
    t1.teleport(250,-200)
    t1.left(90)
    t1.forward(400)
    t1.right(90)
    #Set the little cute turtles
    t1.teleport(-300,150)
    t2.teleport(-300,100)
    t3.teleport(-300,50)
    t4.teleport(-300,0)
    t5.teleport(-300,-50)
    return [t1,t2,t3,t4,t5]
# Function for the turt speed
def race(turtles):
    for i in turtles:
        i.forward(random.randint(0,10))
    return turtles

#Function for which turt won
def whowon(turtles):
    for i in turtles:
        if i.pos()[0] >= 256:
            return i.pencolor()
    return False
# Checking who won
turtlist = setup()
win = False
while not win:
    turtlist = race(turtlist)
    win = whowon(turtlist)
print(f'The {win} turtle won!')
turtle.done()
