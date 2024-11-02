import sqlite3
import pandas as pd

def load_and_aggregate_playlist_tracks(db_path, playlist_id):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Query to select data from the playlist_track table
    query = f"""
    SELECT PlaylistId, TrackId
    FROM playlist_track
    WHERE PlaylistId = {playlist_id}
    """
    
    # Load data into a pandas DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Perform aggregation: count the number of tracks in the playlist
    track_count = df['TrackId'].count()
    
    # Perform filtering: get unique track IDs
    unique_tracks = df['TrackId'].unique()
    
    # Create a result dictionary
    result = {
        'PlaylistId': playlist_id,
        'TrackCount': track_count,
        'UniqueTracks': unique_tracks
    }
    
    return result

# Sample call to the function
db_path = 'data/chinook.db'
playlist_id = 1
result = load_and_aggregate_playlist_tracks(db_path, playlist_id)
print(result)