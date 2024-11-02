import sqlite3

def load_and_aggregate_chinook_sqlite_stat1(db_path):
    """
    Load data from sqlite_stat1 table in the given SQLite database,
    filter out rows where 'idx' is NULL, and aggregate the data by counting
    the number of entries per 'tbl'.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Execute the query to load and filter data
    cursor.execute("""
        SELECT tbl, COUNT(*) as entry_count
        FROM sqlite_stat1
        WHERE idx IS NOT NULL
        GROUP BY tbl
    """)
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return results

# Sample call to the function
db_path = 'data/chinook.db'
aggregated_data = load_and_aggregate_chinook_sqlite_stat1(db_path)
print(aggregated_data)