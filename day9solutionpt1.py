import timeit

#grid = [
#"2199943210",
#"3987894921",
#"9856789892",
#"8767896789",
#"9899965678"
#]

grid = open("2021Day9.txt","r")
grid = [line.strip() for line in grid.readlines()]

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
                    if int(grid[ni][nj]) <= current:
                        is_low_point = False
                        break
            
            if is_low_point:
                low_points.append(current)
    
    return low_points
timer = timeit.Timer(lambda: find_low_points())
print("Elapsed time for find_low_points()",timer.timeit(1))
low_points = find_low_points()
risk_level = sum(point + 1 for point in low_points)
print(f"Risk level: {risk_level}")
