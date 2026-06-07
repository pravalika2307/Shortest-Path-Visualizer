# Project Explanation

## Problem Statement

Finding the shortest path between two nodes is one of the most fundamental graph problems in computer science. This project was built to understand and compare different pathfinding algorithms through practical implementation.

## Existing System

Traditional pathfinding demonstrations are often static and provide limited opportunities for experimentation.

Challenges:

* Limited visualization
* No execution history
* Difficult algorithm comparison


## Proposed System

An interactive web application that allows users to:

* Select different algorithms
* Configure grid dimensions
* Compare path lengths
* Store execution history


## Algorithms Implemented

### Breadth First Search (BFS)

Used for unweighted shortest path discovery.

Time Complexity:

O(V + E)

### Dijkstra's Algorithm

Used for shortest path calculation using cumulative cost.

Time Complexity:

O((V + E) log V)

### A* Search

Uses heuristic guidance for optimized search.

Time Complexity:

O((V + E) log V)


## Results

* Successfully implemented 3 pathfinding algorithms.
* Tested on grids up to 30x30.
* Achieved consistent shortest path computation.
* Integrated persistent history tracking using SQLite.


## Key Learnings

* Graph Theory Fundamentals
* Priority Queue Usage
* Database Integration
* Streamlit Application Development
* GitHub Project Management
