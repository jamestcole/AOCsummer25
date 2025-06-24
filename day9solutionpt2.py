import timeit

grid = open("2021Day9.txt","r")
grid = [line.strip() for line in grid.readlines()]

def find_basin_size(i, j, visited):
    rows = len(grid)
    cols = len(grid[0])
    basin_size = 1
    visited.add((i, j))

    # Check all adjacent positions
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
            if int(grid[ni][nj]) != 9:
                basin_size += find_basin_size(ni, nj, visited)
    
    return basin_size  # Move this outside the loop

def find_low_points():
    low_points = []
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            current = int(grid[i][j])
            is_low_point = True
            
            # Check all adjacent positions
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if current >= int(grid[ni][nj]):
                        is_low_point = False
                        break
            
            if is_low_point:
                low_points.append(current)
    
    return low_points

# Find low points and calculate basin sizes
visited = set()
basin_sizes = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if int(grid[i][j]) != 9 and (i, j) not in visited:
            basin_size = find_basin_size(i, j, visited)
            basin_sizes.append(basin_size)

# Move the sorting and calculation outside the loop
basin_sizes.sort(reverse=True)
top_three_basins = basin_sizes[:3]
result = top_three_basins[0] * top_three_basins[1] * top_three_basins[2]
print("Product of the sizes of the three largest basins:", result)

# Fix the timer and low points calculation
low_points = find_low_points()
risk_level = sum(point + 1 for point in low_points)
print(f"Risk level: {risk_level}")

timer = timeit.Timer(lambda: find_low_points())
print("Elapsed time for find_low_points():", timer.timeit(1))

