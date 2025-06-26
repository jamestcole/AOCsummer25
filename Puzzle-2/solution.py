grid = [
"21999",
"39878",
"98567"
]

def get_neighbours(x,y,height,width,grid):
    neighbours =[]
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny = x+dx,y+dy
        if 0 <= nx < height and 0 <= ny < width:
            neighbours.append((nx,ny,int(grid[nx][ny])))
    return neighbours

def partA():
    height=len(grid)
    width=len(grid[0])
    total_risk=0
    
    for x in range(height):
        for y in range(width):
            current = int(grid[x][y])
            #neighbours of each element
            a_neighbours = get_neighbours(x,y,height,width,grid)
            
            #check low point
            is_low_point = all(current < neighbour_val for _,_,neighbour_val in a_neighbours)
            
            if is_low_point:
                total_risk += current + 1
                
    return total_risk 
    
    
def partB():
    height = len(grid)
    width = len(grid[0])
    visited = set()
    basin_sizes = []
    
    def dfs(x, y):
        if (x, y) in visited or int(grid[x][y]) == 9:
            return 0
        
        visited.add((x, y))
        size = 1
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width:
                size += dfs(nx, ny)
        
        return size
    
    for x in range(height):
        for y in range(width):
            if (x, y) not in visited and int(grid[x][y]) != 9:
                basin_size = dfs(x, y)
                if basin_size > 0:
                    basin_sizes.append(basin_size)
    
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1]


    
##parse input
# with open("input.txt") as file:
#     grid = [list(map(int,line.strip())) for line in file]



# grid = [int(line.strip() for line in grid.readlines())]
    
    
##call partA function    
print(partA())
print(partB())
