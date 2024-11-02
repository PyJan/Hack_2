import sqlite3
import pandas as pd

def return_db_samples():
    tables_dict = {}
    # Connect to the SQLite database
    conn = sqlite3.connect('data/chinook.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query to retrieve all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all results
    tables = cursor.fetchall()

    # Load data from a specific table into a pandas DataFrame
    # Replace 'your_table_name' with the actual table name you want to load
    for table_name in tables:
        table_name = table_name[0]
        tables_dict[table_name] = pd.read_sql_query(f"SELECT * FROM {table_name}", conn).to_csv()

    # Close the connection
    conn.close()

    return tables_dict


if __name__ == '__main__':
    print(return_db_samples())
