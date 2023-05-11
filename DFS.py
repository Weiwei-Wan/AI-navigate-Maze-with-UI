import numpy as np

def DFS_Find_Path(row, col, maze):
    visited = np.zeros((row, col)) # mark the visited cells
    visited[0][0] = 1
    path = [[0,0]]
    choice_ind = [] # save the index (from path) of more than one choice pos
    choices = [] # save the choices of more than one choice pos
    cur = [0,0] # start from [0,0]
    visited_cells = 1
    while cur != [row-1, col-1]:
        # check neighbor
        neighbor = []
        # condition: not edge, not wall, not previous pos
        if cur[0]<row-1 and maze[3*(cur[0]+1), 3*cur[1]+1]==0.5 and visited[cur[0]+1, cur[1]]==0: # down
            neighbor.append([cur[0]+1, cur[1]])
            visited[cur[0]+1, cur[1]] = 1
            visited_cells += 1
        if cur[1]<col-1 and maze[3*cur[0]+1, 3*(cur[1]+1)]==0.5 and visited[cur[0], cur[1]+1]==0: # right
            neighbor.append([cur[0], cur[1]+1])
            visited[cur[0], cur[1]+1] = 1
            visited_cells += 1
        if cur[0]>0 and maze[3*cur[0], 3*cur[1]+1]==0.5 and visited[cur[0]-1, cur[1]]==0: # up
            neighbor.append([cur[0]-1, cur[1]])
            visited[cur[0]-1, cur[1]] = 1
            visited_cells += 1
        if cur[1]>0 and maze[3*cur[0]+1, 3*cur[1]]==0.5 and visited[cur[0], cur[1]-1]==0: # left
            neighbor.append([cur[0], cur[1]-1])
            visited[cur[0], cur[1]-1] = 1
            visited_cells += 1
        # chose next pos
        if len(neighbor) == 1: # only one choice
            cur = [neighbor[0][0], neighbor[0][1]]
            path.append(cur)
        elif len(neighbor) == 0: # no choice, go to latest more than one choices pos
            cur = choices[-1][0]
            path = path[:choice_ind[-1]]
            path.append(cur)
            visited_cells += 1
            if len(choices[-1]) == 1:  # run out of choice, remove from the saving list
                choice_ind = choice_ind[:-1]
                choices = choices[:-1]
            else:
                choices[-1] = choices[-1][1:] # choice - 1
        else: # more than one choice, save it
            cur = [neighbor[0][0], neighbor[0][1]]
            path.append(cur)
            choice_ind.append(len(path)-1)
            choices.append(neighbor[1:])
    return path, visited_cells



