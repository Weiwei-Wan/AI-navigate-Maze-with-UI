from matplotlib import pyplot as plt
from matplotlib.widgets import Button, TextBox
from datetime import datetime 
import copy
import DFS, BFS, AStar, MDP
import GenerateMaze

# defalt value
row = 20
col = 20

# button call back
def click_generate_maze(event):
    global maze
    maze = GenerateMaze.generate_maze(row, col)
    draw_maze()

def click_solve_DFS(event):
    starttime = datetime.now()
    path,_ = DFS.DFS_Find_Path(row, col, maze)
    endtime = datetime.now()
    speed = round((endtime-starttime).total_seconds()*1000, 3)
    ax_button_DFS.set_title(str(speed) + "ms", x=1.5, y=0.1)
    draw_path(path)

def click_solve_BFS(event):
    starttime = datetime.now()
    path,_ = BFS.BFS_Find_Path(row, col, maze)
    endtime = datetime.now()
    speed = round((endtime-starttime).total_seconds()*1000, 3)
    ax_button_BFS.set_title(str(speed) + "ms", x=1.5, y=0.1)
    draw_path(path)

def click_solve_A(event):
    starttime = datetime.now()
    path,_ = AStar.A_Find_Path(row, col, maze)
    endtime = datetime.now()
    speed = round((endtime-starttime).total_seconds()*1000, 3)
    ax_button_A.set_title(str(speed) + "ms", x=1.5, y=0.1)
    draw_path(path)

def click_solve_MDP_value(event):
    starttime = datetime.now()
    path, iter = MDP.MDP_find_path(row, col, maze, 0.9, "value")
    endtime = datetime.now()
    speed = round((endtime-starttime).total_seconds()*1000, 0)
    ax_button_MDP_value.set_title(str(speed) + "ms; Iteration: " + str(iter), x=1.8, y=0.1)
    draw_path(path)

def click_solve_POLICY(event):
    starttime = datetime.now()
    path, iter = MDP.MDP_find_path(row, col, maze, 0.9, "policy")
    endtime = datetime.now()
    speed = round((endtime - starttime).total_seconds()*1000, 0)
    ax_button_POLICY.set_title(str(speed) + "ms; Iteration: " + str(iter), x=1.8, y=0.1)
    draw_path(path)

def clear_path(event):
    draw_maze()

def set_row(num):
    global row
    row = int(num)
    plt.draw()

def set_col(num):
    global col
    col = int(num)
    plt.draw()

def on_change(event):
    plt.draw()

def draw_maze():
    plt.cla()
    plt.axis("off")
    plt.imshow(maze, cmap="RdGy")

def draw_path(path):
    image = copy.deepcopy(maze)
    color = 0.2
    image[1,0] = color
    image[2,0] = color
    for i in range(0, len(path)):
        image[3*path[i][0]+1, 3*path[i][1]+1] = color
        image[3*path[i][0]+1, 3*path[i][1]+2] = color
        image[3*path[i][0]+2, 3*path[i][1]+1] = color
        image[3*path[i][0]+2, 3*path[i][1]+2] = color
        # fill the wall
        if i < len(path)-1:
            if path[i+1][0] == path[i][0]-1: # up
                image[3*path[i][0], 3*path[i][1]+1] = color
                image[3*path[i][0], 3*path[i][1]+2] = color
            elif path[i+1][0] == path[i][0]+1: # down
                image[3*path[i][0]+3, 3*path[i][1]+1] = color
                image[3*path[i][0]+3, 3*path[i][1]+2] = color
            elif path[i+1][1] == path[i][1]-1: # left
                image[3*path[i][0]+1, 3*path[i][1]] = color
                image[3*path[i][0]+2, 3*path[i][1]] = color
            elif path[i+1][1] == path[i][1]+1: # right
                image[3*path[i][0]+1, 3*path[i][1]+3] = color
                image[3*path[i][0]+2, 3*path[i][1]+3] = color
    image[3*row-1, 3*col] = color
    image[3*row-2, 3*col] = color
    plt.cla()
    plt.axis("off")
    plt.imshow(image, cmap="RdGy")

plt.ion()
fig = plt.figure(figsize=(10,8))
fig.canvas.set_window_title("Maze")

# button generate maze
ax_button_generate = plt.axes([0.02, 0.78, 0.15, 0.05])
btn_generate_maze = Button(ax_button_generate, "New maze")
btn_generate_maze.on_clicked(click_generate_maze)

# find path
ax_button_DFS = plt.axes([0.25, 0.92, 0.15, 0.05])
btn_DFS = Button(ax_button_DFS, "DFS Find Path")
btn_DFS.on_clicked(click_solve_DFS)
ax_button_DFS.set_title("- ms", x=1.5, y=0.1)

ax_button_BFS = plt.axes([0.25, 0.85, 0.15, 0.05])
btn_BFS = Button(ax_button_BFS, "BFS Find Path")
btn_BFS.on_clicked(click_solve_BFS)
ax_button_BFS.set_title("- ms", x=1.5, y=0.1)

ax_button_A = plt.axes([0.25, 0.78, 0.15, 0.05])
btn_A = Button(ax_button_A, "A* Find Path")
btn_A.on_clicked(click_solve_A)
ax_button_A.set_title("- ms", x=1.5, y=0.1)

ax_button_MDP_value = plt.axes([0.55, 0.92, 0.18, 0.05])
btn_MDP_value = Button(ax_button_MDP_value, "MDP_VALUE Find Path")
btn_MDP_value.on_clicked(click_solve_MDP_value)
ax_button_MDP_value.set_title("- ms; Iteration:", x=1.8, y=0.1)

ax_button_POLICY = plt.axes([0.55, 0.85, 0.18, 0.05])
btn_POLICY = Button(ax_button_POLICY, "MDP_POLICY Find Path")
btn_POLICY.on_clicked(click_solve_POLICY)
ax_button_POLICY.set_title("- ms; Iteration:", x=1.8, y=0.1)

ax_button_CLEAR = plt.axes([0.55, 0.78, 0.15, 0.05])
btn_CLEAR = Button(ax_button_CLEAR, "CLEAR PATH")
btn_CLEAR.on_clicked(clear_path)

# input row
ax_row_input = plt.axes([0.07, 0.92, 0.06, 0.05])
row_input_box = TextBox(ax_row_input, "row: ", initial=str(row))
row_input_box.on_submit(set_row)
row_input_box.on_text_change(on_change)

# input colum
ax_col_input = plt.axes([0.07, 0.85, 0.06, 0.05])
col_input_box = TextBox(ax_col_input, "colum: ", initial=str(col))
col_input_box.on_submit(set_col)
col_input_box.on_text_change(on_change)

maze = GenerateMaze.generate_maze(row, col)
ax = plt.axes([0.05, 0.0, 0.9, 0.76])
ax.axis('off')
ax.imshow(maze, cmap="RdGy") # 0: red; 0.5: white; 1: black

plt.pause(9999999)