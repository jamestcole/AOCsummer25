
def is_visible(grid,row,col):
    height=grid[row][col]
    rows=len(grid)
    cols=len(grid[0])

    #seeing from left
    blocking_tree=0
    for c in range(col):
        if grid[row][c] >= height:
            blocking_tree+=1
            break
    if blocking_tree==0:
        return True
    
    #seeing from left
    blocking_tree=0
    for c in range(col+1,cols):
        if grid[row][c]>=height:
            blocking_tree+=1
            break
    if blocking_tree==0:
        return True
    
    #seeing from top
    blocking_tree=0
    for r in range(row):
        if grid[r][col]>=height:
            blocking_tree+=1
            break
    if blocking_tree==0:
        return True
    
    #seeing from lbottom
    blocking_tree=0
    for r in range(row+1,rows):
        if grid[r][col]>=height:
            blocking_tree+=1
            break
    if blocking_tree==0:
        return True
    
def get_score(grid,row,col):
    height=grid[row][col]
    rows=len(grid)
    cols=len(grid[0])

    #distance in left
    distance_l=0
    for c in range(col-1,-1,-1):
        distance_l+=1
        if grid[row][c] >= height:
            break
            
    
    #distance in right
    distance_r=0
    for c in range(col+1,cols):
        distance_r+=1
        if grid[row][c]>=height:
            break
        
    #distance in top
    distance_t=0
    for r in range(row-1,-1,-1):
        distance_t+=1
        if grid[r][col]>=height:
            break
    
    #distance in bottom
    distance_b=0
    for r in range(row+1,rows):
        distance_b+=1
        if grid[r][col]>=height:
            break
    
    return distance_b*distance_l*distance_r*distance_t
            
    
def PartA():
    rows=len(grid)
    cols=len(grid[0])
    
    visible_count=0
    
    for row in range(rows):
        for col in range(cols):
            if row==0 or row==rows-1 or col==0 or col==cols-1:
                visible_count+=1
            elif is_visible(grid,row,col):
                visible_count+=1
        
    return visible_count

def PartB():
    rows=len(grid)
    cols=len(grid[0])
    
    max_score=0
    
    for row in range(rows):
        for col in range(cols):
            if row==0 or row==rows-1 or col==0 or col==cols-1:
                score=0
            else:
                score=get_score(grid,row,col)
            max_score=max(score,max_score)
                
        
    return max_score
    
                
with open("input.txt") as file:
    grid = [list(map(int,line.strip())) for line in file]
    
print(PartA())
print(PartB())
