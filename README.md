# AI-navigate-Maze-with-UI

Maze generator UI

Here matplotlib was used to generate a maze of a given size (row, col) using a random depth-first search algorithm. At first I created an image of the maze with walls (black) of size 1 and paths (write) of size 2. Then, from the starting point I visited each cell once using a random depth-first search algorithm to create the only path from the starting point to the end point.

![1](https://github.com/Weiwei-Wan/AI-navigate-Maze-with-UI/assets/74362292/3d226c78-b6c8-4e06-b1df-309aeac8271d)


Implementate 5 algorithms on solving maze 

If run ShowMaze.py, we can generate any size of maze we want. If we click the buttons, we can use the chosen algorithm to find the only path, and the consuming time would also be shown here.

![2](https://github.com/Weiwei-Wan/AI-navigate-Maze-with-UI/assets/74362292/5499deb8-5a5c-4e9d-82bd-971aeeabf284)


Choose parameter for A* algorithm

For the A* algorithm, we need to calculate the heuristic cost, the estimated cost from the current cell to the target cell.  There are two methods to calculate the heuristic cost, Manhattan Distance and Euclidian Distance. Manhattan Distance between two cells is the horizontal plus vertical distance, and the Euclidian Distance is the linear distance between two cells. In A* algorithm, I compared these two heuristic cost calculation methods on three different sizes of maze, result was shown on the below image, each run time and visited cell number are the average of 20 independent maze solving. From the results, when using Manhattan Distance the solving time is slightly faster than using the Euclidian Distance, and the visited cells don’t have  big differences. So, for the A* algorithm, I chose the Manhattan Distance as heuristic cost.

![3](https://github.com/Weiwei-Wan/AI-navigate-Maze-with-UI/assets/74362292/6c869e7a-b241-4c1d-a9f0-8ad7b2c5b76b)


Comparison different gamma in MDP algorithms

In MDP, gamma (γ) represents the discount factor, which is a parameter used to balance the importance of future rewards versus immediate rewards.  A higher γ value means that the agent values future rewards more and will be more willing to take actions that lead to greater long-term rewards, even if they come at the expense of short-term rewards. Here when I chose very small gamma values, sometimes couldn’t generate the right solution, so the tested gamma values start from 0.7,  and in this test all of the generated pathed are correct. From the results shown on the below image, when increasing the gamma value, the consuming time also increases, especially the policy iteration, and the iteration number of value iteration also increases, when gamma = 0.99, the iteration number reaches the maximum 1000. From the result, finally I chose the most common value 0.9.

![4](https://github.com/Weiwei-Wan/AI-navigate-Maze-with-UI/assets/74362292/ed832893-555e-4c4d-b3b6-73b05db31466)


Comparison between 3 search algorithms

To compare the performance of the 3 search algorithms, 3 different sizes of maze were used to test the consuming time and visited cells of the 3 algorithms, and results are shown on the below images. In this case, DFS has the fastest speed, and A* is the slowest between the 3 algorithms. BFS and A* algorithms visited near 80% of all cells, and DFS just visited less than 40% of all cells. And DFS has shown the best performance between these 3 search algorithms.

![5](https://github.com/Weiwei-Wan/AI-navigate-Maze-with-UI/assets/74362292/27b08641-2dc4-4f02-8dad-6d815ef0e6dd)
![6](https://github.com/Weiwei-Wan/AI-navigate-Maze-with-UI/assets/74362292/d31581ad-cf5f-4990-8f76-4050f4376a92)


Comparison between different MDP algorithms

The main difference between policy iteration and value iteration is the way they update the policy and the value function. Policy iteration alternates between policy evaluation and policy improvement. In the policy evaluation step, the algorithm evaluates the current policy by iteratively updating the value function for that policy. In the policy improvement step, the algorithm iteratively updates the policy and value function until convergence. However, value iteration only performs one step of policy evaluation and policy improvement in each iteration.  Value iteration is typically faster than policy iteration, as it only performs one step of policy evaluation and improvement per iteration. However, policy iteration can converge to the optimal policy in fewer iterations than value iteration, as the images shown below.

![7](https://github.com/Weiwei-Wan/AI-navigate-Maze-with-UI/assets/74362292/d8230845-8975-4289-a5ab-c5123187793d)


Comparison between search and MDP algorithms

All of the algorithms mentioned here are effective approaches. The search algorithms are simple and effective for solving maze problems and can be implemented quickly and easily, and it can be more efficient than MDP for small and simple mazes. Here, the time consuming of MDP is more than 1000 fold of the search algorithms. MDP is a more complex algorithm used for solving sequential decision-making problems. MDP can provide the optimal policy for reaching the goal, which means it can guarantee to find the shortest path. MDP can also handle more complex mazes and stochastic environments where there is uncertainty in the result of actions. However, MDP can be computationally expensive and requires more memory and processing power. The choice of algorithm depends on the complexity of the maze, the desired level of accuracy, and the available resources. For small and simple mazes, search algorithms may be more efficient. While for larger and more complex mazes, MDP may be a better choice. However, because of the efficiency of my computer, more complex mazes were not tested.


How to run:

please run ShowMaze.py
the panel shows the maze and algorithms solving the maze

CompareAStar.py, CompareMDP.py, CompareMDPGamma.py, CompareSearchAlgs.py 
are used to generated the comparison figures

DFS.py, BFS.py, AStar.py, MDP.py are algorithms used to solve the mazes
GenerateMaze.py are used to draw maze

Video link: https://youtu.be/afMmOlXJj3w 
