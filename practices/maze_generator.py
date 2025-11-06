#KH 2nd period maze generator
import turtle# import turtle
import random# import random

# Function for making the structual maze1
def maze_generator():
    maze = [[],[],[],[],[]]#make variable for maze
    for c in maze:# Variable for collo
        for i in range(6):#nest
            c.append(random.randint(0,1))
    maze2=[[],[],[],[],[]]# variable for maze 2
    for r in maze2:# another var
        for i in range(6):
            r.append(random.randint(0,1))
    return maze,maze2# return the things

# Function for drawing maze

def drawmaze(rows,cols):# set variables gor rows and collums
    import turtle# Import inside the function
    screen = turtle.Screen()# Set turtle screen
    screen.setup(width=702, height=702)  # Set turtle size
    pen = turtle.Turtle()# Make the pen a turtle
    pen.speed(0)# Set speed super duper fast
    pen.hideturtle()# Hide it because it looks better
    pen.penup()
    pen.teleport(-300,-200)
    for i in rows:# Nest the thing for the thung
        for x in i:
            if x==0:
                pen.penup()
            else:
                pen.pendown()
            pen.forward(100)# The fancy dancy stuff to draw the maze
        pen.penup()
        pen.lt(90)
        pen.forward(100)
        pen.lt(90)
        pen.forward(600)
        pen.rt(180)
    pen.lt(90)
    pen.teleport(-200,-300)
    for i in cols:
        for x in i:
            if x==0:
                pen.penup()
            else:
                pen.pendown()
            pen.forward(100)
        pen.penup()
        pen.rt(90)
        pen.forward(100)
        pen.rt(90)
        pen.forward(600)
        pen.rt(180)
    pen.pendown()
    pen.teleport(-300,-300)
    pen.forward(600)
    pen.rt(90)
    pen.forward(500)
    pen.teleport(300,300)
    pen.rt(90)
    pen.forward(600)
    pen.rt(90)
    pen.forward(500)

    turtle.done()#turtle down
    




# function for checking the maze , #ask ms larose for help
def checkmaze(row_grid, col_grid):
    done=[]# var for the done stuff
    stack=[(0,0)]# var for the stacking stuff
    while stack:# while stack 
        item=random.choice(stack)
        if item==(5,5):# checking if the maze is sovable with the appending thing and just moving ot the next thing.
            return True
        x,y=item[0],item[1]
        if x<5 and col_grid[x][y]==0:
            stack.append((x+1,y))
        if y<5 and row_grid[y][x]==0:
            stack.append((x,y+1))
        if x>0 and col_grid[x-1][y]==0:
            stack.append((x-1,y))
        if y>1 and row_grid[y-1][x]==0:
            stack.append((x,y-1))
        done.append(item)
        for i in done:
            if i in stack:
                stack.remove(i)
    return False
        
#Call all functions
row,col =maze_generator()
while not checkmaze(row, col):
    row,col =maze_generator()
drawmaze(row,col)





