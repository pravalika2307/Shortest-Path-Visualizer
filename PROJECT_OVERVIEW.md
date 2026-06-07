## Abstract:

A grid-based pathfinding tool that visually shows how BFS and Dijkstra explore nodes to find the shortest route between two points. Think a stripped-down Google Maps for a 2D grid.

## Existing Systems This Maps To:

• Google Maps / GPS routing 
• Game AI (enemy navigation) 
• Network packet routing

## Approach:

• Represent the grid as a 2D list; cells are 0 (open) or 1 (wall).
• BFS for unweighted grids — all edges cost 1.
• Dijkstra with heapq for weighted grids.
• Track parent of each node to reconstruct the path.
• Print the explored path as ASCII art in the terminal.