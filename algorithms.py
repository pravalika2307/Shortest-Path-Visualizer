import heapq
from collections import deque

def get_neighbors(node, rows, cols):
    r, c = node

    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    neighbors = []

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr,nc))