import sqlite3
import pandas as pd

def load_and_filter_artists_with_name_containing_substring(db_path: str, substring: str) -> pd.DataFrame:
    """
    Load data from the 'artists' table in the SQLite database, filter artists whose names contain the given substring,
    and return the filtered data as a pandas DataFrame.
    
    :param db_path: Path to the SQLite database file.
    :param substring: Substring to filter artist names.
    :return: Filtered pandas DataFrame.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Query to select artists whose names contain the given substring
    query = f"""
    SELECT * FROM artists
    WHERE Name LIKE '%{substring}%'
    """
    
    # Load the data into a pandas DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    return df

# Sample call to the function
filtered_artists = load_and_filter_artists_with_name_containing_substring('data/chinook.db', 'Santana')
print(filtered_artists)