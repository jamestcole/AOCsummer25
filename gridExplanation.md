# Low Points Detection Algorithm

## Overview
This function identifies "low points" in a 2D grid - positions where the value is strictly smaller than all adjacent neighbors (up, down, left, right).

## Function Signature
```
def find_low_points():
    # Returns a list of values that are low points in the grid
```
## Algorithm Breakdown

### Initialization
```
low_points = []          # List to store found low points
rows = len(grid)         # Total number of rows in the grid
cols = len(grid[0])      # Total number of columns in the grid
```
### Grid Traversal
```
for i in range(rows):
    for j in range(cols):
```
- **Purpose:** Iterate through every position in the 2D grid
- **Complexity:** O(rows × cols) - visits each cell once

### Current Position Analysis
```
current = int(grid[i][j])
is_low_point = True
```
- **current:** Convert grid value to integer for comparison
- **is_low_point:** Assume current position is a low point until proven otherwise

### Adjacent Neighbor Check
```
for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    ni, nj = i + di, j + dj
```
**Direction Vectors:**

- Up: (-1, 0) - Row - 1
- Down: (1, 0) - Row + 1  
- Left: (0, -1) - Col - 1
- Right: (0, 1) - Col + 1

### Boundary Validation & Comparison
```
if 0 <= ni < rows and 0 <= nj < cols:
    if int(grid[ni][nj]) <= current:
        is_low_point = False
        break
```
**Boundary Check:** Ensures neighbor coordinates are within grid bounds

**Low Point Condition:** If ANY neighbor is ≤ current value, it's NOT a low point

### Result Collection
```
if is_low_point:
    low_points.append(current)
```
## Example Walkthrough

### Sample Grid:
```
2  1  9
3  5  6  
9  8  9
```
### Analysis of Position (0,1) - Value: 1
- Up: Out of bounds ✓
- Down: 5 > 1 ✓
- Left: 2 > 1 ✓  
- Right: 9 > 1 ✓

**Result:** Value `1` is a low point!

## Key Characteristics

### Time Complexity
- **O(rows × cols)** - Each cell checked against maximum 4 neighbors

### Space Complexity  
- **O(k)** where k = number of low points found

### Low Point Definition
A position is a **low point** if it's strictly smaller than ALL existing adjacent neighbors.
