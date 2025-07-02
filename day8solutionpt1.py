#grid_raw = """
#30373
#25512
#65332
#33549
#35390
#"""
grid = open("2021Day8.txt","r")
# Parse input
grid = [[int(c) for c in line.strip()] for line in grid.readlines()]
rows = len(grid)
cols = len(grid[0])

def is_visible(r, c):
    val = grid[r][c]
    
    # Check each direction from the cell to the edge
    up    = all(grid[i][c] < val for i in range(0, r))
    down  = all(grid[i][c] < val for i in range(r+1, rows))
    left  = all(grid[r][j] < val for j in range(0, c))
    right = all(grid[r][j] < val for j in range(c+1, cols))
    
    return up or down or left or right

count = 0

for r in range(rows):
    for c in range(cols):
        # Edge cells are always visible
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            count += 1
        else:
            if is_visible(r, c):
                count += 1

print("Visible count:", count)