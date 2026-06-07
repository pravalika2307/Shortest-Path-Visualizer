# Shortest Path Visualizer

Interactive pathfinding visualizer built using:

- BFS
- Dijkstra
- A*

## Features

- Compare multiple algorithms
- Store search history in SQLite
- Interactive Streamlit dashboard
- Recruiter-friendly portfolio project

## Run

pip install -r requirements.txt

streamlit run app.py

## Complexity

| Algorithm | Time | Space |
|-----------|---------------|-------|
| BFS | O(V + E) | O(V) |
| Dijkstra | O((V+E)logV) | O(V) |

## Output

### Home Page

![Home Page](assets/screenshots/home.png)

### BFS Result

![BFS Result](assets/screenshots/bfs-path.png)

### Dijkstra Result

![BFS Result](assets/screenshots/dijkstra-path.png)

### A* Result

![BFS Result](assets/screenshots/astar-path.png)

### History Table

![History](assets/screenshots/search-history.png)