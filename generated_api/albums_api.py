import sqlite3
import pandas as pd

def load_and_aggregate_albums_by_artist(db_path: str, min_album_count: int) -> pd.DataFrame:
    """
    Load album data from the SQLite database, filter artists with a minimum number of albums,
    and aggregate the data to count the number of albums per artist.

    Parameters:
    db_path (str): Path to the SQLite database.
    min_album_count (int): Minimum number of albums an artist must have to be included in the result.

    Returns:
    pd.DataFrame: DataFrame containing artists and their respective album counts.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Query to load album data
    query = """
    SELECT ArtistId, COUNT(AlbumId) as AlbumCount
    FROM albums
    GROUP BY ArtistId
    HAVING COUNT(AlbumId) >= ?
    """
    
    # Load data into a DataFrame
    df = pd.read_sql_query(query, conn, params=(min_album_count,))
    
    # Close the database connection
    conn.close()
    
    return df

# Sample call to the function
db_path = 'data/chinook.db'
min_album_count = 5
result_df = load_and_aggregate_albums_by_artist(db_path, min_album_count)
print(result_df)