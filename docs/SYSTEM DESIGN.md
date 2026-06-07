# System Design

## Architecture

User
↓
Streamlit User Interface
↓
Algorithm Layer
(BFS / Dijkstra / A*)
↓
SQLite Database
↓
Execution History


## Components

### Frontend

* Streamlit Dashboard
* User Input Controls
* Results Visualization


### Algorithm Layer

* BFS
* Dijkstra
* A* Search


### Storage Layer

SQLite Database

Table:

runs

Columns:

* id
* algorithm
* start_node
* end_node
* path_length
* created_at


## Data Flow

1. User selects grid size.
2. User chooses start and end nodes.
3. User selects an algorithm.
4. Algorithm computes shortest path.
5. Result is displayed.
6. Execution details are stored in SQLite.
7. Historical executions are displayed.
