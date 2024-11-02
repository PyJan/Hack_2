import sqlite3

def load_filtered_aggregated_tracks(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL query to filter and aggregate data
    query = """
    SELECT 
        GenreId, 
        COUNT(TrackId) AS TrackCount, 
        AVG(UnitPrice) AS AvgPrice, 
        SUM(Milliseconds) AS TotalDuration
    FROM 
        tracks
    WHERE 
        Milliseconds > 200000
    GROUP BY 
        GenreId
    HAVING 
        TrackCount > 5
    ORDER BY 
        AvgPrice DESC;
    """

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    # Close the connection
    conn.close()

    return results

# Sample call to the function
db_path = 'data/chinook.db'
filtered_aggregated_tracks = load_filtered_aggregated_tracks(db_path)
for row in filtered_aggregated_tracks:
    print(row)