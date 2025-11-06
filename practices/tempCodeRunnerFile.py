def maze_generator():
    maze = [[],[],[],[],[]]
    for c in maze:
        for i in range(6):
            c.append(random.randint(0,1))
    maze2=[[],[],[],[],[]]
    for r in maze2:
        for i in range(6):
            r.append(random.randint(0,1))
    return maze,maze2