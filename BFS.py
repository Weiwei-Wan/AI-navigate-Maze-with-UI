import numpy as np

def BFS_Find_Path(row, col, maze):
    BFSMap = np.zeros((row, col)) # save the step
    step = 1
    BFSMap[0,0] = step
    mission = [[0,0]] # cells with this step
    loop = True
    visited_cells = 1
    while (loop):
        step += 1
        next_mission = [] # to save next step cells
        if mission == []: # no way
            loop = False
            print("NO WAY!!!!")
        else:
            for cur in mission:
                # check neighbors for next step; condition: not edge, not wall, never visited
                if (cur[0]>0 and maze[3*cur[0], 3*cur[1]+1]==0.5 and BFSMap[cur[0]-1, cur[1]]==0): # up
                    BFSMap[cur[0]-1, cur[1]] = step
                    next_mission.append([cur[0]-1, cur[1]])
                    visited_cells += 1
                    if (cur[0]-1==row-1 and cur[1]==col-1): # reach end, stop
                        loop = False
                        break
                if (cur[0]<row-1 and maze[3*(cur[0]+1), 3*cur[1]+1]==0.5 and BFSMap[cur[0]+1, cur[1]]==0): # down
                    BFSMap[cur[0]+1, cur[1]] = step
                    next_mission.append([cur[0]+1, cur[1]])
                    visited_cells += 1
                    if (cur[0]+1==row-1 and cur[1]==col-1):
                        loop = False
                        break
                if (cur[1]>0 and maze[3*cur[0]+1, 3*cur[1]]==0.5 and BFSMap[cur[0], cur[1]-1]==0): # left
                    BFSMap[cur[0], cur[1]-1] = step
                    next_mission.append([cur[0], cur[1]-1])
                    visited_cells += 1
                    if (cur[0]==row-1 and cur[1]-1==col-1):
                        loop = False
                        break
                if (cur[1]<col-1 and maze[3*cur[0]+1, 3*(cur[1]+1)]==0.5 and BFSMap[cur[0], cur[1]+1]==0): # right
                    BFSMap[cur[0], cur[1]+1] = step
                    next_mission.append([cur[0], cur[1]+1])
                    visited_cells += 1
                    if (cur[0]==row-1 and cur[1]+1==col-1):
                        loop = False
                        break
            mission = next_mission
    # generate path
    path = [[row-1, col-1]]
    while (step>1):
        cur = path[-1]
        step -= 1
        # find previous step
        if (cur[0]>0 and BFSMap[cur[0]-1, cur[1]]==step): # up
            path.append([cur[0]-1, cur[1]])
        elif (cur[0]<row-1 and BFSMap[cur[0]+1, cur[1]]==step): # down
            path.append([cur[0]+1, cur[1]])
        elif (cur[1]>0 and BFSMap[cur[0], cur[1]-1]==step): # left
            path.append([cur[0], cur[1]-1])
        elif (cur[1]<col-1 and BFSMap[cur[0], cur[1]+1]==step): # right
            path.append([cur[0], cur[1]+1])
        visited_cells += 1
    path.reverse()
    return path, visited_cells