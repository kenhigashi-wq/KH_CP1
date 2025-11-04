#KH 2nd period maze generator
import turtle
import random

# Function for making the structual maze1
def maze_generator(width, height):
    

# Function for drawing maze
def drawmaze():
    turtle = turtle.Turtle()
    turtle.size = 0
    turtle.pensize(0)
    for i in maze:
        for x in i:
            if x == 1:
                turtle.startfill()





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
            stack.apppend((x+1,y))
        
        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.apppend((x,y+1))
        
        if x > 0 and col_grid[y][x] == 0:
            stack.apppend((x-1,y))
        
        if y > 0 and row_grid[y][x] == 0:
            stack.apppend((x,y-1))
        







