import timeit

def get_highest_scenic_score(grid):
    rows = len(grid)
    cols = len(grid[0])

    def count_visible(r, c, dr, dc):
        """Count visible trees from (r, c) in direction (dr, dc)."""
        height = grid[r][c]
        count = 0
        r += dr
        c += dc
        while 0 <= r < rows and 0 <= c < cols:
            count += 1
            if grid[r][c] >= height:
                break
            r += dr
            c += dc
        return count

    max_score = 0

    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                continue  # Skip edge trees

            up = count_visible(r, c, -1, 0)
            down = count_visible(r, c, 1, 0)
            left = count_visible(r, c, 0, -1)
            right = count_visible(r, c, 0, 1)

            score = up * down * left * right
            if score > max_score:
                max_score = score

    return max_score

# Load grid from file
with open("2021Day8.txt", "r") as f:
    grid = [[int(c) for c in line.strip()] for line in f]

# Run and print result
print("Highest scenic score:", get_highest_scenic_score(grid))

# Time it
timer = timeit.Timer(lambda: get_highest_scenic_score(grid))
print("Time:", timer.timeit(1), "seconds for run")

#Highest scenic score: 422059
#Time: 0.02916479999839794 seconds for run
