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
        # Skip edge trees (they always have score 0)
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            continue

        up = count_visible(r, c, -1, 0)
        down = count_visible(r, c, 1, 0)
        left = count_visible(r, c, 0, -1)
        right = count_visible(r, c, 0, 1)

        score = up * down * left * right
        if score > max_score:
            max_score = score

print("Highest scenic score:", max_score)