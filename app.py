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