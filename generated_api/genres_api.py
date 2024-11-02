import sqlite3
import pandas as pd

def load_and_filter_genres_with_rock_and_aggregate_counts(db_path: str) -> pd.DataFrame:
    """
    Load data from the genres table in the specified SQLite database, filter for genres containing 'Rock',
    and aggregate the counts of such genres.
    
    Parameters:
    db_path (str): Path to the SQLite database file.
    
    Returns:
    pd.DataFrame: DataFrame containing the filtered and aggregated data.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Load the genres table into a DataFrame
    genres_df = pd.read_sql_query("SELECT * FROM genres", conn)
    
    # Filter for genres containing 'Rock'
    filtered_genres_df = genres_df[genres_df['Name'].str.contains('Rock', case=False)]
    
    # Aggregate the counts of such genres
    aggregated_counts = filtered_genres_df.groupby('Name').size().reset_index(name='Count')
    
    # Close the database connection
    conn.close()
    
    return aggregated_counts

# Sample call to the function
db_path = 'data/chinook.db'
result_df = load_and_filter_genres_with_rock_and_aggregate_counts(db_path)
print(result_df)