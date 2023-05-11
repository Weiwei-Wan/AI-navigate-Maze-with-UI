import numpy as np
import random

# draw image for maze (without path); path size: 2; wall size: 1
def draw_mesh(row, col):
    image = np.ones((3*row+1, 3*col+1), dtype=np.uint8)/2
    for i in range(0, row+1):
        image[3*i] = np.ones(3*col+1, dtype=np.uint8)
    for j in range(0, col+1):
        image[::,3*j] = np.ones(3*row+1, dtype=np.uint8)
    image[0, 1] = 0
    # add entrance and exit
    image[1, 0] = 0.5
    image[2, 0] = 0.5
    image[-2, -1] = 0.5
    image[-3, -1] = 0.5
    return image

def generate_maze(row, col):
    image = draw_mesh(row, col)
    # add path from entrance
    path = []
    cur = [0,0]
    visited = np.zeros((row, col))
    visited_num = 0
    while (visited_num<row*col):
        # refresh visited pos
        if (visited[cur[0], cur[1]]==0):
            visited_num += 1
        visited[cur[0], cur[1]] = 1
        choice = []
        # chose a neighbor
        if (cur[0]>0 and visited[cur[0]-1, cur[1]]==0): # up
            choice.append([cur[0]-1, cur[1]])
        if (cur[0]<row-1 and visited[cur[0]+1, cur[1]]==0): # down
            choice.append([cur[0]+1, cur[1]])
        if (cur[1]>0 and visited[cur[0], cur[1]-1]==0): # left
            choice.append([cur[0], cur[1]-1])
        if (cur[1]<col-1 and visited[cur[0], cur[1]+1]==0): # right
            choice.append([cur[0], cur[1]+1])
        # if no neighbor
        if (len(choice)==0):
            # restart last step
            cur = path[-1]
            path = path[ : -1]
        else: # randomly chose a neighbor as next path
            path.append(cur)
            next = choice[random.randint(0, len(choice)-1)]
            # add path (white)
            if (cur[1]==next[1]):
                x = max(cur[0], next[0])
                image[3*x, 3*cur[1]+1] = 0.5
                image[3*x, 3*cur[1]+2] = 0.5
            else:
                y = max(cur[1], next[1])
                image[3*cur[0]+1, 3*y] = 0.5
                image[3*cur[0]+2, 3*y] = 0.5
            cur = next
    return image