import numpy as np

gamma = 0.9
n = 1000 # loop number
threshold = 1e-10

def MDP_find_path(r, c, m, g, type):
    global row, col, maze, gamma, states, actions, random_policy, value_table
    row = r
    col = c
    maze = m
    gamma = g
    states = np.arange(col*row).reshape((row, col))
    random_policy = np.ones((row, col))
    value_table = np.zeros((row, col))
    actions = np.arange(4)
    rewards = -np.ones((row, col))
    rewards[row-1, col-1] = 0 # the end

    if type == "policy":
        best_policy, iter = policy_iteration(random_policy, gamma, n)
    elif type == "value":
        best_policy, iter = value_iteration(value_table, gamma, n)

    # get path
    path = []
    posx = 0
    posy = 0
    next_state = 0
    while not (posx==row-1 and posy==col-1):
        _, next_state, _ = p_state_reward(next_state, best_policy[posx][posy])
        path.append([posx, posy])
        posx = next_state//col
        posy = next_state%col
    path.append([row-1, col-1])
    return path, iter

def p_state_reward(state, action):
    posx = state//col
    posy = state%col
    # up
    if action == 0: 
        if state < col or maze[3*posx, 3*posy+1] != 0.5: # touch wall
            return ((1, state, -1))
        else:
            return ((1, state-col, -1))
    # down
    elif action == 1:
        if state >= col*(row-1) or maze[3*posx+3, 3*posy+1] != 0.5: # touch wall
            return ((1, state, -1))
        elif state == col*(row-1)-1: # reach end
            return ((1, row*col-1, 0))
        else:
            return ((1, state+col, -1))    
    # left
    if action == 2:
        if state%col == 0 or maze[3*posx+1, 3*posy] != 0.5: # touch wall
            return ((1, state, -1))
        else:
            return ((1, state-1, -1))         
    # right
    if action == 3:
        if (state+1)%col == 0 or maze[3*posx+1, 3*posy+3] != 0.5: # touch wall
            return ((1, state, -1))
        elif state == row*col-2: # reach end
            return ((1, row*col-1, 0))
        else:
            return ((1, state+1, -1))

# policy evaluation   
def compute_value_function(policy, gamma):
    values = np.zeros((row, col))
    while True:
        update_values = np.copy(values)
        for i in range(row):
            for j in range(col):
                action = policy[i][j]
                trans_prob, next_state, reward = p_state_reward(states[i][j], action)
                values[i][j] = reward + gamma * trans_prob * update_values[next_state//col][next_state%col]
        if np.sum((np.fabs(update_values - values))) <= threshold:
            break
    return values

def next_best_policy(values, gamma):
    policy = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            action_table = np.zeros(4)
            for action in actions:
                trans_prob, next_state, reward = p_state_reward(states[i][j], action)
                action_table[action] = reward + gamma * trans_prob*values[next_state//col][next_state%col]
            policy[i][j] = np.argmax(action_table) # max element 
    return policy

def policy_iteration(random_policy, gamma, n):
    iter = 0
    for t in range(n):
        iter += 1
        new_value_function = compute_value_function(random_policy, gamma)
        new_policy = next_best_policy(new_value_function, gamma)
        if np.all(random_policy == new_policy):
            break
        random_policy = new_policy      
    return new_policy, iter

def value_iteration(value_table, gamma, n):
    iter = 0
    policy = np.zeros((row, col))
    for t in range(n):
        iter += 1
        update_value_table = np.copy(value_table)
        for i in range(row):
            for j in range(col):
                action_value = np.zeros(len(actions))
                for action in actions:
                    trans_prob, next_state, reward = p_state_reward(states[i][j], action)
                    action_value[action] = reward + gamma * trans_prob * update_value_table[next_state//col][next_state%col]
                value_table[i][j] = max(action_value)
                # best pilicy
                policy[i][j] = np.argmax(action_value)
        if np.sum((np.fabs(update_value_table - value_table))) <= threshold:
            break
    return policy, iter