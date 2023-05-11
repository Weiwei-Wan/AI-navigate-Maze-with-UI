import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime 
import AStar
import GenerateMaze

EuTime = np.zeros((20))
ManTime = np.zeros((20))

EuCells = np.zeros((20))
ManCells = np.zeros((20))

mean_time = []
std_time = []
mean_cell = []
std_cell = []

labels = ['Manhattan Distance', 'Euclidian Distance']
error_params=dict(elinewidth=1,capsize=4)
maze_list = [20, 50, 100]

for r in maze_list:
    row = r
    col = r
    for i in range(20):
        maze = GenerateMaze.generate_maze(row, col)
        time1 = datetime.now()
        path,cells = AStar.A_Find_Path(row, col, maze)
        time2 = datetime.now()
        ManTime[i] = (time2-time1).total_seconds()*1000
        ManCells[i] = cells

        time1 = datetime.now()
        path,cells = AStar.A_Find_Path_Eu(row, col, maze)
        time2 = datetime.now()
        EuTime[i] = (time2-time1).total_seconds()*1000
        EuCells[i] = cells

    mean_time.append([np.mean(ManTime), np.mean(EuTime)])
    std_time.append([np.std(ManTime, ddof=1), np.std(EuTime, ddof=1)])
    mean_cell.append([np.mean(ManCells), np.mean(EuCells)])
    std_cell.append([np.std(ManCells, ddof=1), np.std(EuCells, ddof=1)])

print(mean_time)
print(mean_cell)
n = 0
fig = plt.figure(figsize=(10,6))
for r in maze_list:
    row = r
    col = r
    n += 1
    plt.subplot(1,3,n)
    plt.bar(range(len(mean_time[n-1])), mean_time[n-1], yerr=std_time[n-1], error_kw=error_params, tick_label=labels, width=0.5)
    plt.xticks(rotation = 20)
    plt.xlabel('Heuristic')
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
    plt.bar(range(len(mean_cell[n-1])), mean_cell[n-1], yerr=std_cell[n-1], error_kw=error_params, tick_label=labels, width=0.5)
    plt.xticks(rotation = 20)
    plt.xlabel('Heuristic')
    if n == 1:
        plt.ylabel('Visted cells')
    plt.title("row = " + str(row) + ", column = " + str(col))
    plt.grid(True,axis='y',ls=':',color='b',alpha=0.3)
plt.show()

        


