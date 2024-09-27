# problem:
# https://csacademy.com/contest/interview-archive/task/largest-matrix-zone/

# result: 100%
# my code, enhance by chatgpt to overcome 
# the non zero exit code error (due to recursion limit in python)

# -------------------------------------------------------------------------------
# Addressing the Non-Zero Exit Code Issue:
# The non-zero exit code error you're encountering is likely due to
# Python's recursion depth limit being exceeded when processing large inputs.
# The flood fill algorithm uses recursion, which can cause a stack overflow 
# if the matrix is large or has a complex pattern of connected 1s.
# To fix this, you can replace the recursive flood fill with an 
# iterative approach using a stack (depth-first search) or
# a queue (breadth-first search). This avoids hitting Python's recursion limit.

# Here’s the modified code with an iterative flood fill using a stack

# Iterative flood fill to count zone size
from typing import List, Tuple

def initiate_flood_fill(array2d: List[List[int]], ir: int, ic: int, row: int, col: int, prev_color: int, color: int) -> int:
    stack = [(ir, ic)]
    size = 0
    is_valid_zone = True

    while stack:
        cr, cc = stack.pop()

        # Skip if out of bounds or not matching the color we're flooding
        if cr < 0 or cr >= row or cc < 0 or cc >= col or array2d[cr][cc] != prev_color:
            continue
        
        # If touching the border, invalidate this zone
        if cr == 0 or cr == row - 1 or cc == 0 or cc == col - 1:
            is_valid_zone = False
        
        # Color the current cell and increment size
        array2d[cr][cc] = color
        size += 1

        # Push neighbors to the stack
        stack.append((cr-1, cc))  # Up
        stack.append((cr+1, cc))  # Down
        stack.append((cr, cc-1))  # Left
        stack.append((cr, cc+1))  # Right

    return size if is_valid_zone else 0

# Program input
R, C = map(int, input().split())

matrix = []
for _ in range(R):
    a = list(map(int, input().split()))
    matrix.append(a)

zones = []

# Flood fill for each unvisited cell with '1'
for i in range(1, R-1):  # Skip first and last row
    for j in range(1, C-1):  # Skip first and last column
        if matrix[i][j] == 1:
            zone_size = initiate_flood_fill(matrix, i, j, R, C, 1, 2)
            if zone_size > 0:
                zones.append(zone_size)

# Output the largest zone, or -1 if no valid zones found
if zones:
    print(max(zones))
else:
    print(-1)
