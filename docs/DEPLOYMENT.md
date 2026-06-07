# Deployment Guide

## Local Setup

Clone the repository:

git clone <https://github.com/pravalika2307/Shortest-Path-Visualizer.git>

Navigate to the project folder:

cd shortest-path-visualizer

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py


## Streamlit Cloud Deployment

1. Push the project to GitHub.
2. Login to Streamlit Cloud.
3. Create a new application.
4. Connect the GitHub repository.
5. Select the main branch.
6. Choose app.py as the entry point.
7. Deploy the application.


## Dependencies

* Streamlit
* Pandas
* SQLite (built into Python)


## Database

The application automatically creates:

path_history.db

during first execution and stores algorithm execution history.
