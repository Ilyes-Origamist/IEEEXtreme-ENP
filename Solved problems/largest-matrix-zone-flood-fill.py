# problem:
# https://csacademy.com/contest/interview-archive/task/largest-matrix-zone/

# result: 66.67%
# non zero exit code errors: due to python recursion limits. 
# see the second code to get 100% result (code adjusted by chatgpt)

from typing import List, Tuple

# Flood fill to count zone size
def initiate_flood_fill(array2d: List[List[int]], ir: int, ic: int, row: int, col: int, prev_color: int, color: int) -> int:
    i = [0]  # Counter as a list to allow modification inside recursive calls
    is_valid_zone = [True]  # Track whether this zone touches the border
    flood_fill(array2d, ir, ic, row, col, prev_color, color, i, is_valid_zone)
    return i[0] if is_valid_zone[0] else 0

# DFS flood fill algorithm with border check
def flood_fill(array2d: List[List[int]], ir: int, ic: int, row: int, col: int, prev_color: int, color: int, i: List[int], is_valid_zone: List[bool]):
    if ir < 0 or ir >= row or ic < 0 or ic >= col:
        return
    if array2d[ir][ic] != prev_color:
        return

    # If touching the border, invalidate this zone
    if ir == 0 or ir == row-1 or ic == 0 or ic == col-1:
        is_valid_zone[0] = False
    
    array2d[ir][ic] = color
    i[0] += 1

    # Recursive calls in all four directions
    flood_fill(array2d, ir-1, ic, row, col, prev_color, color, i, is_valid_zone)  # Up
    flood_fill(array2d, ir+1, ic, row, col, prev_color, color, i, is_valid_zone)  # Down
    flood_fill(array2d, ir, ic-1, row, col, prev_color, color, i, is_valid_zone)  # Left
    flood_fill(array2d, ir, ic+1, row, col, prev_color, color, i, is_valid_zone)  # Right

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