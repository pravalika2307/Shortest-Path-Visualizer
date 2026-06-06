import sqlite3

DB_NAME = "path_history.db"

def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS runs
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    algorithm TEXT,
                    start_node TEXT,
                    end_node TEXT,
                    path_length INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
                )

    conn.commit()

    conn.close()

def save_run(algorithm, start_node, end_node, path_length):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""INSERT INTO runs
                   (algorithm,
                   start_node,
                   end_node,
                   path_length)
                   VALUES(?,?,?,?)""",
                (algorithm,
                str(start_node),
                str(end_node),
                path_length)
                )

    conn.commit()

    conn.close()

def get_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()