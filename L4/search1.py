# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    closed=[[0 for row in range(len(grid[0]))] for col in range(len(grid[0]))]
    closed[init[0]][init[1]]=1
    x=init[0]
    y=init[1]
    g=0
    
    open=[[g,x,y]]
    
    found=False # set when search is complete
    resign=False # set if we can't find expand
        
    while found is False and resign is False:
        
        #check for oppen elements on the open list
        if len(open)==0:
            resign=True
            return 'fail'
        else:
            #remove node from list
            open.sort()
            open.reverse()
            next=open.pop()
          #  print next
            x=next[1]
            y=next[2]
            g=next[0]
            
              #check if we are done
            if x==goal[0] and y==goal[1]:
                found=True
                return next
            else:
              #expanding winning element and add to new open list
                for i in range(len(delta)):
                    x2=x+delta[i][0]
                    y2=y+delta[i][1]
                    if x2>=0 and x2<len(grid) and y2>=0 and y2 < len(grid[0]):
                        if closed[x2][y2]==0 and grid[x2][y2]==0:
                            g2=g +cost
                            open.append([g2,x2,y2])
                            closed[x2][y2]=1


print search(grid,init,goal,cost)