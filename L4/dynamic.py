# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    nodes = [goal]
    value = [[99 for rows in range(len(grid[0]))] for cols in range(len(grid))]
    closed = [[0 for rows in range(len(grid[0]))] for cols in range(len(grid))]
    g = 0
    value[goal[0]][goal[1]] = g;
    
    while len(nodes) != 0:
        node = nodes.pop(0)
        x = node[0]
        y = node[1]
        closed[x][y] = 1
    
        for i in range(len(delta)):
            x2 = x - delta[i][0]
            y2 = y - delta[i][1]
    
            if (x2>=0) and (y2>=0) and (x2 <= (len(grid)-1)) and (y2 <= (len(grid[0])-1)):
                if grid[x2][y2] == 0 and closed[x2][y2] == 0:
                    nodes.append([x2,y2])
                    value[x2][y2] = value[x][y]+cost
    
     
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 


print compute_value(grid,goal,cost)