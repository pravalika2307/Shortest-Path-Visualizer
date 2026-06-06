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
    
    return neighbors


def bfs(rows, cols, start, end):

    queue = deque([(start,[start])])

    visited = {start}

    while queue:

        node, path = queue.popleft()

        if node == end:
            return path

        for neighbor in get_neighbors(node, rows, cols):

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append((neighbor, path + [neighbor]))

    return []

def dijkstra(rows, cols, start, end):

    heap = [(0,start)]

    distances = {start:0}

    parent = {start:None}

    while heap:

        cost,node = heapq.heappop(heap)

        if node == end:

            path = []

            while node:

                path.append(node)

                node = parent[node]

            return path[::-1]
        
        for neighbor in get_neighbors(node, rows, cols):

            new_cost = cost + 1

            if (neighbor not in distances or new_cost < distances[neighbor]):

                distances[neighbor] = new_cost

                parent[neighbor] = node

                heapq.heappush(heap,(new_cost,neighbor))

    return []

def heuristic(a,b):

    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(rows, cols, start, end):

    heap = [(0,start)]

    g_score = {start:0}

    parent = {start:None}

    while heap:

        _,node = heapq.heappop(heap)

        if node == end:

            path = []

            while node:

                path.append(node)

                node = parent[node]

            return path[::-1]

        for neighbor in get_neighbors(node, rows, cols):

            tentative = g_score[node] + 1

            if (neighbor not in g_score or tentative < g_score[neighbor]):

                g_score[neighbor] = tentative

                f_score = tentative + heuristic(neighbor,end)

                parent[neighbor] = node

                heapq.heappush(heap,(f_score,neighbor))

    return []
