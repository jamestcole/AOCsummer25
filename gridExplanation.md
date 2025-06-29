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

### Adjacent Neighbor Check - Detailed Explanation
```
for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    ni, nj = i + di, j + dj
```
#### How the Direction Vectors Work

**The List of Tuples:**
```
[(-1, 0), (1, 0), (0, -1), (0, 1)]
```
Each tuple represents a direction to move from the current position:
- **First number (di):** Change in row (i direction)
- **Second number (dj):** Change in column (j direction)

#### Tuple Unpacking Process

**Iteration 1:** di = -1, dj = 0
- Moving UP: decrease row by 1, column stays same
- ni = i + (-1) = i - 1
- nj = j + 0 = j

**Iteration 2:** di = 1, dj = 0  
- Moving DOWN: increase row by 1, column stays same
- ni = i + 1
- nj = j + 0 = j

**Iteration 3:** di = 0, dj = -1
- Moving LEFT: row stays same, decrease column by 1
- ni = i + 0 = i
- nj = j + (-1) = j - 1

**Iteration 4:** di = 0, dj = 1
- Moving RIGHT: row stays same, increase column by 1  
- ni = i + 0 = i
- nj = j + 1

#### Concrete Example

**If current position is (2, 3):**
- i = 2 (row 2)
- j = 3 (column 3)

**Checking each neighbor:**

1. **UP:** di = -1, dj = 0
   - ni = 2 + (-1) = 1
   - nj = 3 + 0 = 3
   - **Neighbor position: (1, 3)**

2. **DOWN:** di = 1, dj = 0
   - ni = 2 + 1 = 3  
   - nj = 3 + 0 = 3
   - **Neighbor position: (3, 3)**

3. **LEFT:** di = 0, dj = -1
   - ni = 2 + 0 = 2
   - nj = 3 + (-1) = 2
   - **Neighbor position: (2, 2)**

4. **RIGHT:** di = 0, dj = 1
   - ni = 2 + 0 = 2
   - nj = 3 + 1 = 4
   - **Neighbor position: (2, 4)**

#### Grid Coordinate System

**Visual representation:**
    j→  0  1  2  3  4
i ↓
0      [0,0][0,1][0,2][0,3][0,4]
1      [1,0][1,1][1,2][1,3][1,4]  
2      [2,0][2,1][2,2][2,3][2,4]  ← Current: (2,3)
3      [3,0][3,1][3,2][3,3][3,4]

**From position (2,3), the neighbors are:**
- UP: (1,3) - one row above
- DOWN: (3,3) - one row below  
- LEFT: (2,2) - one column left
- RIGHT: (2,4) - one column right

#### Why This Method Works

**Advantages:**
- **Systematic:** Checks all 4 cardinal directions
- **Efficient:** Single loop handles all neighbor checks
- **Clean:** No duplicate code for each direction
- **Extensible:** Easy to add diagonal directions by adding more tuples like (-1,-1), (-1,1), (1,-1), (1,1)

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

2  1  9
3  5  6  
9  8  9

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