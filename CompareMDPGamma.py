import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime 
import MDP, DFS
import GenerateMaze

row = 10
col = 10

valueTime = np.zeros((10))
policyTime = np.zeros((10))

valueIter = np.zeros((10))
policyIter = np.zeros((10))

value_mean_time = []
value_std_time = []
value_mean_iter = []
value_std_iter = []

policy_mean_time = []
policy_std_time = []
policy_mean_iter = []
policy_std_iter = []

labels = ['Value', 'Policy']
error_params=dict(elinewidth=1,capsize=4)

gamma_list = [0.7, 0.8, 0.9, 0.95, 0.99]
for gamma in gamma_list:
    for i in range(10):
        maze = GenerateMaze.generate_maze(row, col)
        real_path,_ = DFS.DFS_Find_Path(row, col, maze)
        time1 = datetime.now()
        path,Iter = MDP.MDP_find_path(row, col, maze, gamma, "value")
        time2 = datetime.now()
        valueTime[i] = (time2-time1).total_seconds()*1000
        valueIter[i] = Iter
        print(gamma)
        print("value: ")
        print(path == real_path)
        time1 = datetime.now()
        path,Iter = MDP.MDP_find_path(row, col, maze, gamma, "policy")
        time2 = datetime.now()
        policyTime[i] = (time2-time1).total_seconds()*1000
        policyIter[i] = Iter
        print("policy")
        print(path == real_path)
    
    policy_mean_time.append(np.mean(policyTime))
    policy_std_time.append(np.std(policyTime, ddof=1))
    policy_mean_iter.append(np.mean(policyIter))
    policy_std_iter.append(np.std(policyIter, ddof=1))
    print(gamma)
    value_mean_time.append(np.mean(valueTime))
    value_std_time.append(np.std(valueTime, ddof=1))
    value_mean_iter.append(np.mean(valueIter))
    value_std_iter.append(np.std(valueIter, ddof=1))
    print("22222222")

print(value_mean_iter)
print(policy_mean_iter)

fig = plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.errorbar(gamma_list, policy_mean_time, c="b", yerr=policy_std_time, label="policy")
plt.errorbar(gamma_list, value_mean_time, c="g", yerr=value_std_time, label="value")
plt.xlabel('gamma')
plt.ylabel('Run time (ms)')
plt.grid(True,axis='y',ls=':',color='b',alpha=0.3)
plt.legend()

plt.subplot(1,2,2)
plt.errorbar(gamma_list, policy_mean_iter, c="b", yerr=policy_std_iter, label="policy")
plt.errorbar(gamma_list, value_mean_iter, c="g", yerr=value_std_iter, label="value")
plt.xlabel('gamma')
plt.ylabel('Iteration')
plt.grid(True,axis='y',ls=':',color='b',alpha=0.3)
plt.legend()

plt.show()

        


