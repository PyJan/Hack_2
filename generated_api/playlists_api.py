import sqlite3
import pandas as pd

def load_and_filter_aggregate_playlists(db_path, filter_name=None, aggregate_by='Name'):
    """
    Load data from the playlists table, filter by name if provided, and aggregate by the specified column.
    
    Parameters:
    db_path (str): Path to the SQLite database.
    filter_name (str): Name to filter the playlists by. If None, no filtering is applied.
    aggregate_by (str): Column name to aggregate the data by.
    
    Returns:
    pd.DataFrame: Aggregated DataFrame.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Load data from the playlists table
    query = "SELECT * FROM playlists"
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Filter by name if filter_name is provided
    if filter_name:
        df = df[df['Name'].str.contains(filter_name, case=False)]
    
    # Aggregate by the specified column
    aggregated_df = df.groupby(aggregate_by).size().reset_index(name='Count')
    
    return aggregated_df

# Sample call to the function
db_path = 'data/chinook.db'
result = load_and_filter_aggregate_playlists(db_path, filter_name='Music', aggregate_by='Name')
print(result)