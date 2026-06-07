import streamlit as st
import pandas as pd

from algorithms import bfs
from algorithms import dijkstra
from algorithms import astar

from database import create_table
from database import save_run
from database import get_history

create_table()

st.set_page_config(page_title="Shortest Path Visualizer", layout="wide")

st.title("Shortest Path Visualizer")

st.sidebar.header("Controls")

rows = st.sidebar.slider("Rows", 5, 30, 10)

cols = st.sidebar.slider("Columns", 5, 30, 10)

start_row = st.sidebar.number_input("Start Row", 0,rows-1, 0)

start_col = st.sidebar.number_input("Start Col", 0, cols-1, 0)

end_row = st.sidebar.number_input("End Row", 0, rows-1, rows-1)

end_col = st.sidebar.number_input("End Col", 0, cols-1, cols-1)

algorithm = st.sidebar.selectbox("Algorithm",["BFS", "Dijkstra", "A*"])

if st.button("Find Path"):

    start = (start_row,start_col)
    end = (end_row,end_col)

    if algorithm == "BFS":
        path = bfs(rows,cols,start,end)

    elif algorithm == "Dijkstra":
        path = dijkstra(rows,cols,start,end)

    else:
        path = astar(rows,cols,start,end)

    st.success(f"Path Found ({len(path)-1} steps)")

    st.write(path)

    save_run(algorithm, start, end, len(path)-1)