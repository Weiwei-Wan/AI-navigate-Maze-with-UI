import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime 
import DFS, BFS, AStar
import GenerateMaze

DFSTime = np.zeros((20))
BFSTime = np.zeros((20))
AStarTime = np.zeros((20))

DFSCells = np.zeros((20))
BFSCells = np.zeros((20))
AStarCells = np.zeros((20))

mean_time = []
std_time = []
mean_cell = []
std_cell = []

labels = ['DFS', 'BFS', 'A*']
error_params=dict(elinewidth=1,capsize=4)
maze_list = [20, 50, 100]

for r in maze_list:
    row = r
    col = r
    for i in range(20):
        maze = GenerateMaze.generate_maze(row, col)
        time1 = datetime.now()
        path,cells = DFS.DFS_Find_Path(row, col, maze)
        time2 = datetime.now()
        DFSTime[i] = (time2-time1).total_seconds()*1000
        DFSCells[i] = cells

        time1 = datetime.now()
        path,cells = BFS.BFS_Find_Path(row, col, maze)
        time2 = datetime.now()
        BFSTime[i] = (time2-time1).total_seconds()*1000
        BFSCells[i] = cells

        time1 = datetime.now()
        path,cells = AStar.A_Find_Path(row, col, maze)
        time2 = datetime.now()
        AStarTime[i] = (time2-time1).total_seconds()*1000
        AStarCells[i] = cells

    mean_time.append([np.mean(DFSTime), np.mean(BFSTime), np.mean(AStarTime)])
    std_time.append([np.std(DFSTime, ddof=1), np.std(BFSTime, ddof=1), np.std(AStarTime, ddof=1)])
    mean_cell.append([np.mean(DFSCells), np.mean(BFSCells), np.mean(AStarCells)])
    std_cell.append([np.std(DFSCells, ddof=1), np.std(BFSCells, ddof=1), np.std(AStarCells, ddof=1)])

print(mean_time)
print(mean_cell)
n = 0
fig = plt.figure(figsize=(10,5))
for r in maze_list:
    row = r
    col = r
    n += 1
    plt.subplot(1,3,n)
    plt.bar(range(len(mean_time[n-1])), mean_time[n-1], yerr=std_time[n-1], error_kw=error_params, tick_label=labels,)
    plt.xlabel('Search algorithms')
    if n == 1:
        plt.ylabel('Run time (ms)')
    plt.title("row = " + str(row) + ", column = " + str(col))
    plt.grid(True,axis='y',ls=':',color='b',alpha=0.3)
plt.show()

n = 0
fig = plt.figure(figsize=(12,6))
for r in maze_list:
    row = r
    col = r
    n += 1
    plt.subplot(1,3,n)
    plt.bar(range(len(mean_cell[n-1])), mean_cell[n-1], yerr=std_cell[n-1], error_kw=error_params, tick_label=labels,)
    plt.xlabel('Search algorithms')
    if n == 1:
        plt.ylabel('Visted cells')
    plt.title("row = " + str(row) + ", column = " + str(col))
    plt.grid(True,axis='y',ls=':',color='b',alpha=0.3)
plt.show()

        


