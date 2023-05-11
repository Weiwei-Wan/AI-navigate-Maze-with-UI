import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime 
import MDP
import GenerateMaze

valueTime = np.zeros((10))
policyTime = np.zeros((10))

valueIter = np.zeros((10))
policyIter = np.zeros((10))

mean_time = []
std_time = []
mean_iter = []
std_iter = []

labels = ['Value', 'Policy']
error_params=dict(elinewidth=1,capsize=4)
maze_list = [5, 10, 20]

for r in maze_list:
    row = r
    col = r
    for i in range(10):
        maze = GenerateMaze.generate_maze(row, col)
        time1 = datetime.now()
        path,Iter = MDP.MDP_find_path(row, col, maze, 0.9, "value")
        time2 = datetime.now()
        valueTime[i] = (time2-time1).total_seconds()*1000
        valueIter[i] = Iter

        time1 = datetime.now()
        path,Iter = MDP.MDP_find_path(row, col, maze, 0.9, "policy")
        time2 = datetime.now()
        policyTime[i] = (time2-time1).total_seconds()*1000
        policyIter[i] = Iter
        print(i)
    
    mean_time.append([np.mean(valueTime), np.mean(policyTime)])
    std_time.append([np.std(valueTime, ddof=1), np.std(policyTime, ddof=1)])
    mean_iter.append([np.mean(valueIter), np.mean(policyIter)])
    std_iter.append([np.std(valueIter, ddof=1), np.std(policyIter, ddof=1)])

print(mean_time)
print(mean_iter)
n = 0
fig = plt.figure(figsize=(10,5))
for r in maze_list:
    row = r
    col = r
    n += 1
    plt.subplot(1,3,n)
    plt.bar(range(len(mean_time[n-1])), mean_time[n-1], yerr=std_time[n-1], error_kw=error_params, tick_label=labels, width=0.5)
    plt.xlabel('MDP')
    if n == 1:
        plt.ylabel('Run time (ms)')
    plt.title("row = " + str(row) + ", column = " + str(col))
    plt.grid(True,axis='y',ls=':',color='b',alpha=0.3)
plt.show()

n = 0
fig = plt.figure(figsize=(10,5))
for r in maze_list:
    row = r
    col = r
    n += 1
    plt.subplot(1,3,n)
    plt.bar(range(len(mean_iter[n-1])), mean_iter[n-1], yerr=std_iter[n-1], error_kw=error_params, tick_label=labels,width=0.5)
    plt.xlabel('MDP')
    if n == 1:
        plt.ylabel('Iteration')
    plt.title("row = " + str(row) + ", column = " + str(col))
    plt.grid(True,axis='y',ls=':',color='b',alpha=0.3)
plt.show()

        


