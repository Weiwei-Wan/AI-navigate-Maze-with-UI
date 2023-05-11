import queue
import numpy as np
import math

# Manhattan Distance
def A_Find_Path(row, col, maze):
    f_score = np.ones((row, col))*float("inf")
    g_score = np.ones((row, col))*float("inf")
    q = queue.PriorityQueue() # use PriorityQueue to choose path with the smallest f_score
    path_map = {} # use map to save the path
    g_score[0,0] = 0
    h_score = col+row-2
    f_score[0,0] = g_score[0,0] + h_score # add Manhattan Distance
    q.put([f_score[0,0], h_score, [0,0]])
    visited_cells = 1
    while (not q.empty()):
        cur = q.get()[2] # always choice pos with the smallest f_score
        # check neighbor; condition: not edge, not wall, has smaller f_score
        h_score = col+row-2-(cur[0]-1+cur[1])
        if (cur[0]>0 and maze[3*cur[0], 3*cur[1]+1]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0]-1, cur[1]]): # up
            g_score[cur[0]-1, cur[1]] = g_score[cur[0], cur[1]]+1  # compute new g_score and f_score
            f_score[cur[0]-1, cur[1]] = g_score[cur[0]-1, cur[1]]+h_score # add Manhattan Distance
            q.put([f_score[cur[0]-1, cur[1]], h_score, [cur[0]-1, cur[1]]]) # add to queue
            path_map[str(cur[0]-1)+str("/")+str(cur[1])] = cur # save where current pos come from
            visited_cells += 1
            if (cur[0]-1==row-1 and cur[1]==col-1): # reach end, stop
                break
        h_score = col+row-2-(cur[0]+1+cur[1])
        if (cur[0]<row-1 and maze[3*(cur[0]+1), 3*cur[1]+1]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0]+1, cur[1]]): # down
            g_score[cur[0]+1, cur[1]] = g_score[cur[0], cur[1]]+1
            f_score[cur[0]+1, cur[1]] = g_score[cur[0]+1, cur[1]]+h_score
            q.put([f_score[cur[0]+1, cur[1]], h_score, [cur[0]+1, cur[1]]])
            path_map[str(cur[0]+1)+str("/")+str(cur[1])] = cur
            visited_cells += 1
            if (cur[0]+1==row-1 and cur[1]==col-1):
                break
        h_score = col+row-2-(cur[0]-1+cur[1])
        if (cur[1]>0 and maze[3*cur[0]+1, 3*cur[1]]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0], cur[1]-1]): # left
            g_score[cur[0], cur[1]-1] = g_score[cur[0], cur[1]]+1
            f_score[cur[0], cur[1]-1] = g_score[cur[0], cur[1]-1]+h_score
            q.put([f_score[cur[0], cur[1]-1], h_score, [cur[0], cur[1]-1]])
            path_map[str(cur[0])+str("/")+str(cur[1]-1)] = cur
            visited_cells += 1
            if (cur[0]==row-1 and cur[1]-1==col-1):
                break
        h_score = col+row-2-(cur[0]+1+cur[1])
        if (cur[1]<col-1 and maze[3*cur[0]+1, 3*(cur[1]+1)]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0], cur[1]+1]): # right
            g_score[cur[0], cur[1]+1] = g_score[cur[0], cur[1]]+1
            f_score[cur[0], cur[1]+1] = g_score[cur[0], cur[1]+1]+h_score
            q.put([f_score[cur[0], cur[1]+1], h_score, [cur[0], cur[1]+1]])
            path_map[str(cur[0])+str("/")+str(cur[1]+1)] = cur
            visited_cells += 1
            if (cur[0]==row-1 and cur[1]+1==col-1):
                break
        if (q.empty()):
            print("NO WAY!!!")
    # get path
    path = []
    cur = str(row-1)+str("/")+str(col-1)
    path.append([row-1, col-1])
    while cur in path_map:
        visited_cells += 1
        path.append(path_map[cur])
        cur = str(path_map[cur][0])+str("/")+str(path_map[cur][1])
    path.reverse()
    return path, visited_cells

# Euclidian Distance
def A_Find_Path_Eu(row, col, maze):
    f_score = np.ones((row, col))*float("inf")
    g_score = np.ones((row, col))*float("inf")
    q = queue.PriorityQueue() # use PriorityQueue to choose path with the smallest f_score
    path_map = {} # use map to save the path
    g_score[0,0] = 0
    h_score = math.sqrt((row-1)*(row-1) + (col-1)*(col-1)) # add Euclidian Distance
    f_score[0,0] = g_score[0,0] + h_score 
    q.put([f_score[0,0], h_score, [0,0]])
    visited_cells = 1
    while (not q.empty()):
        cur = q.get()[2] # always choice pos with the smallest f_score
        # check neighbor; condition: not edge, not wall, has smaller f_score
        h_score = math.sqrt((row-cur[0])*(row-cur[0]) + (col-1-cur[1])*(col-1-cur[1]))
        if (cur[0]>0 and maze[3*cur[0], 3*cur[1]+1]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0]-1, cur[1]]): # up
            g_score[cur[0]-1, cur[1]] = g_score[cur[0], cur[1]]+1  # compute new g_score and f_score
            f_score[cur[0]-1, cur[1]] = g_score[cur[0]-1, cur[1]]+h_score 
            q.put([f_score[cur[0]-1, cur[1]], h_score, [cur[0]-1, cur[1]]]) # add to queue
            path_map[str(cur[0]-1)+str("/")+str(cur[1])] = cur # save where current pos come from
            visited_cells += 1
            if (cur[0]-1==row-1 and cur[1]==col-1): # reach end, stop
                break
        h_score = math.sqrt((row-cur[0]-2)*(row-cur[0]-2) + (col-1-cur[1])*(col-1-cur[1]))
        if (cur[0]<row-1 and maze[3*(cur[0]+1), 3*cur[1]+1]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0]+1, cur[1]]): # down
            g_score[cur[0]+1, cur[1]] = g_score[cur[0], cur[1]]+1
            f_score[cur[0]+1, cur[1]] = g_score[cur[0]+1, cur[1]]+h_score
            q.put([f_score[cur[0]+1, cur[1]], h_score, [cur[0]+1, cur[1]]])
            path_map[str(cur[0]+1)+str("/")+str(cur[1])] = cur
            visited_cells += 1
            if (cur[0]+1==row-1 and cur[1]==col-1):
                break
        h_score = math.sqrt((row-cur[0]-1)*(row-cur[0]-1) + (col-cur[1])*(col-cur[1]))
        if (cur[1]>0 and maze[3*cur[0]+1, 3*cur[1]]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0], cur[1]-1]): # left
            g_score[cur[0], cur[1]-1] = g_score[cur[0], cur[1]]+1
            f_score[cur[0], cur[1]-1] = g_score[cur[0], cur[1]-1]+h_score
            q.put([f_score[cur[0], cur[1]-1], h_score, [cur[0], cur[1]-1]])
            path_map[str(cur[0])+str("/")+str(cur[1]-1)] = cur
            visited_cells += 1
            if (cur[0]==row-1 and cur[1]-1==col-1):
                break
        h_score = math.sqrt((row-cur[0]-1)*(row-cur[0]-1) + (col-cur[1]-2)*(col-cur[1]-2))
        if (cur[1]<col-1 and maze[3*cur[0]+1, 3*(cur[1]+1)]==0.5 and (g_score[cur[0], cur[1]]+1+h_score)<f_score[cur[0], cur[1]+1]): # right
            g_score[cur[0], cur[1]+1] = g_score[cur[0], cur[1]]+1
            f_score[cur[0], cur[1]+1] = g_score[cur[0], cur[1]+1]+h_score
            q.put([f_score[cur[0], cur[1]+1], h_score, [cur[0], cur[1]+1]])
            path_map[str(cur[0])+str("/")+str(cur[1]+1)] = cur
            visited_cells += 1
            if (cur[0]==row-1 and cur[1]+1==col-1):
                break
        if (q.empty()):
            print("NO WAY!!!")
    # get path
    path = []
    cur = str(row-1)+str("/")+str(col-1)
    path.append([row-1, col-1])
    while cur in path_map:
        visited_cells += 1
        path.append(path_map[cur])
        cur = str(path_map[cur][0])+str("/")+str(path_map[cur][1])
    path.reverse()
    return path, visited_cells
