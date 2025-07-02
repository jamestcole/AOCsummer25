import timeit

def get_visible_count(grid):
    rows = len(grid)
    cols = len(grid[0])

    def is_visible(r, c):
        val = grid[r][c]

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

    return count

# Load grid
with open("2021Day8.txt", "r") as f:
    grid = [[int(c) for c in line.strip()] for line in f]

# Run and print result
print("Visible count:", get_visible_count(grid))

# Time it
timer = timeit.Timer(lambda: get_visible_count(grid))
print("Time:", timer.timeit(number=1), "seconds for run")

#Visible count: 1693
#Time: 0.08861619999515824 seconds for run
