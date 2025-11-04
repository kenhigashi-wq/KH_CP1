#KH 2nd period maze generator
import turtle
import random

# Function for making the structual maze1
def maze_generator():
    maze = [[],[],[],[],[],[],[]]
    for c in maze:
        for i in range(7):
            c.append(random.randint(0,1))
    maze2=[[],[],[],[],[],[],[]]
    for r in maze2:
        for i in range(7):
            r.append(random.randint(0,1))
    return maze,maze2

# Function for drawing maze

def drawmaze(rows,cols):
    import turtle
    screen = turtle.Screen()
    screen.setup(width=702, height=702)  
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.teleport(-350,-400)
    for i in rows:
        for x in i:
            if x==0:
                pen.penup()
            else:
                pen.pendown()
            pen.forward(100)
        pen.penup()
        pen.lt(90)
        pen.forward(100)
        pen.lt(90)
        pen.forward(700)
        pen.rt(180)
    pen.rt(90)
    pen.teleport(350,350)
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
        pen.forward(700)
        pen.rt(180)
    pen.pendown()
    pen.teleport(-350,-350)
    pen.rt(180)
    pen.forward(700)
    pen.rt(90)
    pen.forward(600)
    pen.teleport(350,350)
    pen.rt(90)
    pen.forward(700)
    pen.rt(90)
    pen.forward(600)

    turtle.done()
    




# function for checking the maze
def checkmaze(row_grid, col_grid):
    size = len(row_grid) - 1# checking the size
    visited = set()# Recoding where it went
    stack = [(0,0)]# the stack

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size - 1:
            return True

        if (x,y) in visited:
            continue
# do the visited thing
        visited.add((x,y))
# Do the right left up and down
        if x < size - 1 and col_grid[y][x+1] == 0:
            stack.append((x+1,y))
        
        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.append((x,y+1))
        
        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1,y))
        
        if y > 0 and row_grid[y][x] == 0:
            stack.append((x,y-1))
        

row,col =maze_generator()
while not checkmaze(row, col):
    row,col =maze_generator()
drawmaze(row,col)





